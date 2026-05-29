#!/usr/bin/env python3
"""
Google Flow Connector — uploads Neurocents production documents to Google Drive.

First run: opens a browser for OAuth consent. Saves token.json locally.
Subsequent runs: uses the cached token (refreshes automatically).

Usage:
    python google_flow_connector.py                         # dry-run (preview only)
    python google_flow_connector.py --upload                # upload all files
    python google_flow_connector.py --upload --images       # also upload generated images
    python google_flow_connector.py --upload --force        # re-upload even if file exists
"""

import argparse
import json
import mimetypes
import os
import re
import sys

SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = "token.json"
CREDENTIALS_FILE = "credentials.json"
DRIVE_ROOT_FOLDER = "Neurocents — Production"

# Map filename prefix → (video number, display title)
VIDEO_MAP = {
    "Dopamine_Trap":       (1,  "V01 — Dopamine Trap"),
    "Bandwidth_Tax":       (2,  "V02 — Bandwidth Tax"),
    "Iowa_Gambling":       (3,  "V03 — Iowa Gambling Task"),
    "Mental_Accounting":   (4,  "V04 — Mental Accounting"),
    "Peak":                (5,  "V05 — Peak"),
    "Status_Quo":          (6,  "V06 — Status Quo Bias"),
    "Treadmill":           (7,  "V07 — Someone Needs You to Buy at the Top"),
    "Anchor":              (8,  "V08 — Getting Rich Is Making You Poorer"),
    "Neurocents_Keywords": (0,  "_Channel — Keywords"),
}

# Fallback MIME type for unknown extensions
DEFAULT_MIME = "application/octet-stream"


def _mime(path: str) -> str:
    t, _ = mimetypes.guess_type(path)
    return t or DEFAULT_MIME


def _get_creds():
    """Return valid Google credentials, running the OAuth flow if needed."""
    try:
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        print(
            "Missing Google client libraries.\n"
            "Install with:  pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib"
        )
        sys.exit(1)

    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(
                    f"credentials.json not found.\n"
                    f"Download it from Google Cloud Console → APIs & Services → Credentials\n"
                    f"(OAuth 2.0 Client ID, Desktop app type) and place it here as '{CREDENTIALS_FILE}'."
                )
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as fh:
            fh.write(creds.to_json())
        print(f"Token saved → {TOKEN_FILE}")

    return creds


def _build_service(creds):
    from googleapiclient.discovery import build
    return build("drive", "v3", credentials=creds)


def _find_or_create_folder(service, name: str, parent_id: str | None = None) -> str:
    """Return the Drive folder ID for `name` under `parent_id`, creating it if absent."""
    q = f"name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
    if parent_id:
        q += f" and '{parent_id}' in parents"

    resp = service.files().list(q=q, fields="files(id,name)", spaces="drive").execute()
    items = resp.get("files", [])
    if items:
        return items[0]["id"]

    meta = {"name": name, "mimeType": "application/vnd.google-apps.folder"}
    if parent_id:
        meta["parents"] = [parent_id]
    folder = service.files().create(body=meta, fields="id").execute()
    return folder["id"]


def _file_exists(service, name: str, parent_id: str) -> str | None:
    """Return file ID if a non-trashed file with this name already exists in the folder."""
    q = f"name='{name}' and '{parent_id}' in parents and trashed=false"
    resp = service.files().list(q=q, fields="files(id)", spaces="drive").execute()
    items = resp.get("files", [])
    return items[0]["id"] if items else None


def _upload_file(service, local_path: str, parent_id: str, force: bool = False) -> str:
    """Upload a local file to Drive under parent_id. Returns the file ID."""
    from googleapiclient.http import MediaFileUpload

    filename = os.path.basename(local_path)
    existing_id = _file_exists(service, filename, parent_id)

    if existing_id and not force:
        print(f"  SKIP  {filename}  (already exists)")
        return existing_id

    media = MediaFileUpload(local_path, mimetype=_mime(local_path), resumable=True)

    if existing_id and force:
        file = service.files().update(fileId=existing_id, media_body=media).execute()
        print(f"  UPDATE {filename}")
    else:
        meta = {"name": filename, "parents": [parent_id]}
        file = service.files().create(body=meta, media_body=media, fields="id").execute()
        print(f"  UPLOAD {filename}")

    return file["id"]


def collect_files(base_dir: str) -> dict[str, list[str]]:
    """
    Scan base_dir for generated documents and group them by video folder name.
    Returns {folder_label: [absolute_path, ...]}
    """
    groups: dict[str, list[str]] = {}

    for fname in sorted(os.listdir(base_dir)):
        if not (fname.endswith(".docx") or fname.endswith(".pdf")):
            continue

        full_path = os.path.join(base_dir, fname)
        matched = False

        for prefix, (_, label) in VIDEO_MAP.items():
            if fname.startswith(prefix):
                groups.setdefault(label, []).append(full_path)
                matched = True
                break

        if not matched:
            groups.setdefault("_Misc", []).append(full_path)

    return groups


def dry_run(groups: dict[str, list[str]]) -> None:
    print(f"\nDRY RUN — would create folder '{DRIVE_ROOT_FOLDER}/' in Google Drive\n")
    for label in sorted(groups):
        print(f"  {DRIVE_ROOT_FOLDER}/{label}/")
        for path in groups[label]:
            print(f"    {os.path.basename(path)}")
    total = sum(len(v) for v in groups.values())
    print(f"\n  {total} files across {len(groups)} folders")
    print("\nRun with --upload to sync to Google Drive.")


def upload(groups: dict[str, list[str]], force: bool = False) -> None:
    creds = _get_creds()
    service = _build_service(creds)

    print(f"\nEnsuring root folder '{DRIVE_ROOT_FOLDER}' …")
    root_id = _find_or_create_folder(service, DRIVE_ROOT_FOLDER)
    print(f"  Root folder ID: {root_id}")

    for label in sorted(groups):
        print(f"\n{label}/")
        folder_id = _find_or_create_folder(service, label, root_id)
        for path in groups[label]:
            _upload_file(service, path, folder_id, force=force)

    total = sum(len(v) for v in groups.values())
    print(f"\nDone — {total} files processed.")
    print(f"Open Drive: https://drive.google.com/drive/folders/{root_id}")


def collect_images(base_dir: str) -> dict[str, list[str]]:
    """Scan the images/ subfolder and group PNGs by video folder."""
    groups: dict[str, list[str]] = {}
    images_dir = os.path.join(base_dir, "images")
    if not os.path.isdir(images_dir):
        return groups
    for video_folder in sorted(os.listdir(images_dir)):
        folder_path = os.path.join(images_dir, video_folder)
        if not os.path.isdir(folder_path):
            continue
        pngs = sorted(
            os.path.join(folder_path, f)
            for f in os.listdir(folder_path)
            if f.endswith(".png")
        )
        if pngs:
            groups[f"Images — {video_folder}"] = pngs
    return groups


def main() -> None:
    parser = argparse.ArgumentParser(description="Sync Neurocents docs to Google Drive.")
    parser.add_argument("--upload", action="store_true", help="Actually upload files (default: dry-run)")
    parser.add_argument("--images", action="store_true", help="Also upload generated images from images/ folder")
    parser.add_argument("--force", action="store_true", help="Re-upload files that already exist in Drive")
    parser.add_argument("--dir", default=os.path.dirname(os.path.abspath(__file__)),
                        help="Directory to scan (default: script directory)")
    args = parser.parse_args()

    groups = collect_files(args.dir)
    if args.images:
        groups.update(collect_images(args.dir))

    if not groups:
        print("No .docx or .pdf files found. Run the build scripts first.")
        sys.exit(0)

    if args.upload:
        upload(groups, force=args.force)
    else:
        dry_run(groups)


if __name__ == "__main__":
    main()
