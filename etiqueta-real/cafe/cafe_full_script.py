# -*- coding: utf-8 -*-
"""CAFE - Full script text (V3), section by section.
REESCRITO DE CERO tomando como plantilla directa de densidad y ritmo el
guion outlier de ground beef (10 marcas a evitar + 8 que aguantan, ~29 min).
Estructura: 10 marcas a evitar + 5 mejores opciones, countdown directo,
2-3 datos fechados y apilados por entrada, frases cortas, cero relleno."""

HOOK = """El café es el segundo producto más comprado cada semana en los supermercados de España y Latinoamérica, justo después del pan. Y la mayoría de la gente que lo compra no tiene ni idea de qué empresa hay realmente detrás del paquete que tiene en la mano.

El 24 de agosto de 2025, un grupo estadounidense dueño de los refrescos 7Up y Dr Pepper firmó un cheque de quince mil setecientos millones de euros. A cambio se llevó, de golpe, tres marcas de café que llevan décadas vendiéndose en el mismo lineal como si compitieran entre sí: Marcilla, Saimaza y L'Or. Sin cambio de etiqueta. Sin ningún aviso al consumidor. El paquete tuvo exactamente el mismo aspecto al día siguiente.

Este vídeo repasa diez marcas de café que probablemente deberías reconsiderar, y cinco que sí aguantan el análisis con datos reales, no con la palabra "premium" en la caja. Empezamos por las peores y terminamos con las que de verdad merecen la pena. La primera marca de esta lista, casi con toda seguridad, ya está en tu cocina ahora mismo."""

MARCA10 = """Número diez. Bonka.

Nestlé la describe, en su propia web corporativa, como una de "nuestras marcas locales" de café en España. Junto a ella coloca otro nombre, Eko, con el mismo objetivo de marketing: sonar cercano, casi de barrio, sin ningún apellido de multinacional visible en el envase.

Bonka es Nestlé. La misma compañía que fabrica Nescafé, el café instantáneo más vendido del planeta, con presencia en más de ciento ochenta países. No hay ninguna empresa española independiente detrás del nombre Bonka desde hace décadas.

Esto no la convierte automáticamente en un mal café. El problema es otro, y es puramente de decisión de compra: mucha gente elige Bonka en el lineal precisamente para evitar comprar Nescafé, por la sensación de estar apoyando algo distinto a la gran multinacional suiza. Si esa fue tu razón alguna vez, nunca saliste de la empresa que creías estar evitando. Solo cambiaste de pasillo dentro del mismo edificio.

Nestlé no se detiene en dos nombres. Entre café soluble, cápsulas compatibles y café molido, controla en España varias marcas más que no llevan su apellido en ningún sitio visible del envase. El lineal tampoco ayuda a que lo notes: Nescafé y Bonka se colocan casi siempre en zonas separadas de la estantería, con packaging, tipografía y colores completamente distintos. La misma persona, en la misma sede en Suiza, firma el precio de las dos cada trimestre."""

MARCA9 = """Número nueve. Marcilla. Fundada en España en 1892, más de ciento treinta años de historia real detrás del nombre.

Durante décadas perteneció a la neerlandesa Douwe Egberts, después integrada en JDE Peet's junto a L'Or, Senseo y Jacobs. Ya era, desde mucho antes de que tú lo supieras, parte de un conglomerado internacional cotizado en bolsa, no el negocio familiar de toda la vida que sugiere su publicidad con olor a cafetera de la abuela.

El 24 de agosto de 2025 pasó algo bastante más grande. Keurig Dr Pepper, el grupo estadounidense que fabrica 7Up, Dr Pepper y las cápsulas Keurig, cerró un acuerdo para comprar el cien por cien de JDE Peet's a treinta y un euros con ochenta y cinco céntimos por acción. Precio total: quince mil setecientos millones de euros, más de dieciocho mil millones de dólares, en efectivo. La operación se completó en 2026. El plan, anunciado el mismo día, es partir la empresa combinada en dos compañías nuevas que cotizarán por separado en Estados Unidos.

Keurig Dr Pepper ya puso nombre y cara a quien dirigirá ese negocio del café: Rafael Oliveira, anunciado como consejero delegado de la futura "Global Coffee Co." antes incluso de que la compra terminara de cerrarse. Un ejecutivo con nombre, cargo y fecha de nombramiento público, dirigiendo desde ahora una marca que en el envase de tu cocina sigue pareciendo cien por cien española.

Para Keurig Dr Pepper, la lógica financiera es sencilla: comprar de golpe una cartera de marcas con más de un siglo de confianza ya construida sale más barato que levantar una marca nueva compitiendo contra Nestlé en Europa desde cero. La confianza que tú sientes por Marcilla es, ahora mismo, literalmente un activo que aparece valorado en euros en un comunicado de prensa, y que cambió de dueño sin que a ti te consultaran nada."""

MARCA8 = """Número ocho. Saimaza. Nacida en Sevilla en 1908, fundada por Joaquín Sáinz de la Maza. El nombre de la marca es literalmente una contracción de su propio apellido: Sáinz de la Maza, Saimaza.

Hacia 1935, apenas veintisiete años después, ya figuraba como el tercer mayor importador de café de España, con una producción declarada de cinco mil kilos diarios. En 1937 se constituyó formalmente como sociedad anónima. Más de un siglo de recorrido empresarial real, no una etiqueta inventada por un departamento de marketing la semana pasada.

Y sin embargo, mismo destino final que Marcilla, empresa por empresa y fecha por fecha: acabó integrada en Douwe Egberts, después en JDE Peet's, y el 24 de agosto de 2025, junto con Marcilla y L'Or, a manos de Keurig Dr Pepper en la misma operación de quince mil setecientos millones de euros. El mismo comunicado de prensa, el mismo día, las tres marcas de golpe, sin distinguir entre la que tiene ciento diecisiete años de historia y la que tiene treinta y tres.

Mucha gente alterna entre Marcilla y Saimaza en la misma casa, convencida de estar variando entre dos negocios que compiten de verdad por su dinero. Desde agosto de 2025, comprar cualquiera de las dos es, contablemente, la misma transacción hacia la misma matriz estadounidense.

La publicidad de cada una refuerza esa separación a propósito, y lleva haciéndolo décadas. Los anuncios de Saimaza apuestan por el norte, el carácter, la intensidad del grano tostado fuerte. Los de Marcilla, por la familia, la tradición, la mesa de toda la vida. Dos guiones de marketing completamente distintos, financiados desde el mismo presupuesto corporativo, diseñados para dos públicos que la empresa matriz sabe perfectamente que no se solapan del todo en el supermercado."""

MARCA7 = """Número siete. Hacendado, la marca blanca de Mercadona.

Mercadona no tuesta café. Lo produce a través de sus interproveedores, empresas externas que fabrican en exclusiva para la cadena. Para gran parte de la gama de café soluble, ese fabricante es Prosol, con sede en Venta de Baños, Palencia, fundada en 1998. Prosol cerró 2025 con ciento sesenta millones ochocientas mil euros de facturación, un nueve por ciento más que el año anterior, y opera ya en más de treinta países, alcanzando a catorce millones de consumidores diarios, de los cuales casi nueve millones están fuera de España.

Para el café en grano y molido, el fabricante es otro completamente distinto: UCC Coffee Spain, filial de una multinacional japonesa con sede en Kobe. Hasta enero de 2021, la línea de café americano de Hacendado se producía en Japón y se importaba entera hasta España. Desde esa fecha se fabrica en Logroño, con una inversión declarada de más de doscientos cincuenta mil euros. El cambio no alteró absolutamente nada en la etiqueta, en la receta ni en el precio del paquete.

Ni "Prosol" ni "UCC Coffee Spain" aparecen impresos en ningún sitio del envase. Solo ves "Hacendado", presentado de forma que la mayoría de compradores asume, sin que nadie se lo diga explícitamente, que Mercadona lo fabrica ella misma. Mercadona es la cadena con más cuota de mercado de España, y esa fuerza de compra le permite presionar el precio de sus interproveedores hacia abajo cada año. Esa presión casi nunca se traduce en mejor calidad declarada del grano en el envase."""

CTA = """Si esto ya te está haciendo mirar distinto el paquete de café que tienes en la cocina, dale al botón de suscribirte para no perderte el próximo análisis. Seguimos, porque las siete marcas que quedan es donde el mecanismo se pone bastante más serio."""

MARCA6 = """Número seis. La marca blanca genérica de café molido: Carrefour, Dia, Lidl, Alcampo, o la cadena equivalente en tu país.

Ninguna tuesta su propio café. Todas contratan a un puñado de torrefactoras industriales que fabrican, en la misma nave y a veces literalmente la misma semana, el café que después termina bajo media docena de marcas distintas y precios distintos. La normativa permite declarar el origen con fórmulas genéricas cuando no hay un proveedor único y estable.

Aquí está la palabra que decide todo, y que el Real Decreto 1676/2012 obliga por ley a imprimir en cada paquete de café vendido en España: natural, torrefacto, o mezcla. La costumbre nace de una patente muy concreta, con fecha exacta: el 21 de diciembre de 1901, el empresario extremeño José Gómez Tejedor registró la patente del café torrefacto en España, después de ver en sus viajes a Cuba y México cómo los mineros añadían azúcar al café verde para protegerlo de la humedad y alargar su conservación. La patente le daba veinte años de exclusividad. En 1930 fue nombrado proveedor oficial de la Casa Real española. Su empresa, la tostadora La Estrella, sigue existiendo hoy. Y hoy, La Estrella es propiedad de Nestlé, la misma compañía que ya viste en Bonka y que vas a volver a ver en un momento.

El torrefacto se popularizó de verdad en la posguerra de los años cuarenta, cuando el café era caro y escaso: de un kilo de café verde con azúcar añadida se obtiene hasta uno coma dos kilos de producto final tostado, un truco de rendimiento, no de sabor. El proceso puede usar hasta quince kilos de azúcar por cada cien kilos de café. Esa caramelización a alta temperatura genera acrilamida, un compuesto que estudios de laboratorio asocian a efectos negativos en concentraciones elevadas, y que ha llevado a la organización Justicia Alimentaria a pedir directamente el fin del torrefacto en España. Es, además, una práctica prácticamente inexistente fuera de España y algunas zonas de Portugal y Latinoamérica: el resto de Europa lo considera, directamente, un defecto de fábrica. Buena parte de las marcas blancas venden por defecto precisamente esa mezcla, sin que la palabra "torrefacto" destaque nunca en la parte frontal del paquete."""

MARCA5 = """Número cinco. Nescafé, propiedad de Nestlé, la misma casa que ya viste en Bonka y en la tostadora La Estrella.

Nescafé nació en 1938, después de que el gobierno brasileño le pidiera a Nestlé, ya en 1930, resolver un problema que no tenía nada que ver con el sabor: Brasil tenía un excedente de café tan enorme que no sabía qué hacer con él, y los precios se hundían. El químico suizo Max Morgenthaler tardó siete años en encontrar una forma estable de conservarlo en polvo. El café soluble nació como la solución a una crisis agrícola brasileña, no como la búsqueda de la mejor taza posible.

Para convertir grano en polvo instantáneo, el café pasa por extracción a alta presión y después por un secado que elimina buena parte de sus compuestos aromáticos originales, los mismos que muchas marcas reponen después con aromas añadidos declarados en la etiqueta bajo la Directiva europea 1999/4/CE. No es ilegal, ni es un secreto oculto. Es, sencillamente, lo que ese proceso industrial sacrifica por diseño desde 1938.

En 2025, la Procuraduría Federal del Consumidor de México, Profeco, analizó en laboratorio veintinueve productos de café soluble buscando específicamente maíz o garbanzo añadido, siguiendo la norma NMX-F-139. Ninguna de las diecinueve marcas cien por cien café dio positivo en almidón. Pero el organismo sí señaló con nombre propio a una marca, Golden Hills: su versión mezclada con azúcar registró un trece coma ocho por ciento de azúcares totales, y su versión descafeinada, un nueve coma seis por ciento, muy por encima del resto de la muestra analizada ese mismo año."""

MARCA4 = """Número cuatro. L'Or. Cápsulas de aluminio, diseño elegante, precio muy superior por taza frente al café molido de la misma casa matriz.

A diferencia de Marcilla y Saimaza, L'Or no tiene un siglo de historia real detrás. Nació en Francia en 1992, creada desde cero por el mismo grupo neerlandés, con el objetivo declarado de fijar un nuevo estándar en el segmento premium. No cruzó la frontera francesa hasta 2010. Todo el prestigio "de toda la vida" que transmite su packaging dorado tiene, en realidad, poco más de tres décadas, la mitad de las que lleva funcionando Bonka.

Aquí se cierra un círculo que ya conoces de dos entradas atrás. L'Or pertenecía al mismo grupo, JDE Peet's, que ya viste en Marcilla y Saimaza. El 24 de agosto de 2025, Keurig Dr Pepper se llevó las tres marcas en la misma operación, el mismo día, por el mismo cheque de quince mil setecientos millones de euros: la tradicional de 1892, la de Sevilla de 1908, y la premium de cápsula de 1992.

Si en tu casa alguien compra Marcilla entre semana y guarda L'Or para las visitas "porque es mejor café", ambas decisiones de compra terminan, desde 2025, en exactamente la misma empresa matriz estadounidense. Quince mil setecientos millones de euros por L'Or, Marcilla y Saimaza juntas es, sobre todo, una entrada directa y de golpe al mercado europeo del café en cápsula, el segmento que más margen deja de todo el sector del café envasado. Keurig Dr Pepper no compró historia ni tradición. Compró cuota de mercado ya construida durante más de un siglo por otros."""

MARCA3 = """Número tres. Café Bustelo y Café Pilón, dos marcas que se venden en las mismas estanterías de comunidades latinas en Estados Unidos y el Caribe, con packaging, colores y personalidad de marca completamente distintos y hasta rivales entre sí en el imaginario del comprador.

Café Bustelo lo fundó en 1928 un inmigrante asturiano, Gregorio Menéndez Bustelo, que había pasado antes por Cuba y llegó a Nueva York en 1917. Abrió su primera tostadora en la Quinta Avenida, en pleno East Harlem, el barrio conocido como "El Barrio". Durante los años treinta, Gregorio vendió su café puerta a puerta a bodegas latinas y pequeños comercios del barrio, tratando a cada dueño de tienda, según la propia historia oficial de la marca, "como familia". Ese origen de inmigrante construyendo confianza calle a calle es exactamente lo que la marca sigue vendiendo hoy en su publicidad.

Bustelo y Pilón pertenecían a Rowland Coffee Roasters, una empresa familiar de Miami que también fabricaba Café Oquendo, Medaglia d'Oro y El Pico. El 16 de mayo de 2011, casi un siglo después de que Gregorio abriera su tostadora en El Barrio, The J.M. Smucker Company, la misma multinacional de Ohio que fabrica las mermeladas Smucker's y la crema de cacahuete Jif, completó la compra de Rowland entera por trescientos sesenta millones de dólares, en efectivo. La operación se anunció y se cerró en cuestión de semanas.

Bustelo y Pilón, que llevan décadas presentándose como opciones rivales del mismo pasillo de café cubano, son desde ese mayo de 2011 exactamente la misma empresa. No son solo dos marcas del mismo dueño: son dos identidades culturales completas, construidas durante generaciones por familias cafeteras cubanas, que ahora responden a la misma sala de juntas en Orrville, Ohio, sede corporativa de Smucker's, a más de dos mil kilómetros de Miami."""

MARCA2 = """Número dos. Colcafé, orgullo cafetero de Colombia, fundada en Medellín en 1950.

Colcafé es hoy el negocio de café de Grupo Nutresa, líder del mercado colombiano en café tostado y molido, presente en más de setenta países. Hasta aquí, una historia limpia de éxito industrial colombiano de posguerra.

Pero desde marzo de 2025, quien controla Grupo Nutresa, y con él Colcafé, tiene nombre y apellido: Jaime Gilinski Bacal, banquero colombiano-británico. El 17 de marzo de 2025, en junta de accionistas, Gilinski se convirtió en propietario absoluto de Nugil, el vehículo de inversión con el que había lanzado una OPA hostil sobre Nutresa ya en noviembre de 2021. Nugil controla el treinta y cuatro coma ochenta y uno por ciento de las acciones de Nutresa, lo que convierte a Gilinski en beneficiario final de más del ochenta y cuatro por ciento de toda la compañía. La operación de control final se financió con dos mil millones de dólares.

Gilinski es el mismo empresario que en el Reino Unido controla el banco Metro Bank, y en Colombia, Bancolombia, el mayor banco del país. Cuando compras una lata de Colcafé, una parte de ese dinero entra en el patrimonio de un banquero con activos financieros en tres continentes, tras una batalla accionarial de casi cuatro años que rompió la vieja estructura cruzada de empresas antioqueñas que llevaba controlando Nutresa desde hacía décadas. Nada de esto es ilegal ni está oculto: es información pública, publicada en cualquier informe de la Superintendencia Financiera colombiana. Simplemente no está impresa en la lata de café."""

MARCA1 = """Número uno. Cualquier café descafeinado que no especifique el método de descafeinado en el envase. El más común, y el que casi con toda seguridad tienes en casa si compras descafeinado de supermercado, usa disolventes químicos: cloruro de metileno o acetato de etilo.

Es el método más barato y más usado de la industria desde hace décadas. El grano verde se sumerge en el disolvente el tiempo suficiente para arrastrar la mayoría de la cafeína. Siempre queda un residuo, habitualmente en torno al cero coma uno por ciento, dentro de los límites que fija el Reglamento europeo CE 1999/4 y que agencias como la FDA consideran seguros a esos niveles.

Pero el debate está abierto, con fecha y con nombre propio. En diciembre de 2023, el Environmental Defense Fund y otras organizaciones presentaron una petición formal a la FDA para prohibir el cloruro de metileno como aditivo alimentario. La FDA sometió esa prohibición a consulta pública en enero de 2024. La EPA ya prohibió buena parte de sus usos industriales en abril de 2024. La decisión final sobre el café, a día de hoy, sigue sin cerrarse. Mientras tanto, el proceso también produce, según especialistas del sector, un café más plano, con menos matices aromáticos y un regusto artificial reconocible.

La alternativa existe desde hace décadas, cuesta más, y casi ninguna marca de supermercado la usa: el proceso Swiss Water, que elimina hasta el noventa y nueve coma nueve por ciento de la cafeína usando solo agua y carbón activado, sin ningún disolvente químico de por medio. Si el paquete no dice qué método usó, la apuesta razonable es que fue el químico, no el de agua. El precio, casi nunca la etiqueta, suele ser la única pista real que tienes en el lineal."""

MEJORES_INTRO = """Si esto te está ayudando a ver el pasillo del café de otra forma, comparte el vídeo con quien jura que "su marca es distinta a todas las demás". Ahora sí, las cinco que aguantan el análisis con datos, no con la palabra impresa en la caja."""

MEJOR5 = """Mejor opción número cinco. Café de especialidad con tueste natural: aquí hablamos de una categoría entera, no de una marca concreta.

Busca en el envase "cien por cien arábica" y "tueste natural" de forma explícita, y evita "torrefacto" o "mezcla" sin porcentaje declarado al lado. Los torrefactores de proximidad, cada vez más numerosos en España y Latinoamérica, publican la puntuación de su café según la escala de la Specialty Coffee Association, de cero a cien puntos, donde solo por encima de ochenta se considera oficialmente "de especialidad". El dato suele venir con la fecha de tueste impresa, no solo una fecha de caducidad genérica a dos años vista, porque el grano de especialidad pierde aroma en semanas, no en meses. Ninguna de las diez marcas anteriores publica ese dato en ningún sitio de su envase, sencillamente porque ninguna compite en esa categoría de mercado."""

MEJOR4 = """Mejor opción número cuatro. El método Swiss Water, para quien concretamente busca descafeinado.

Frente al disolvente químico que viste en el puesto número uno de la lista de evitar, este proceso elimina la cafeína usando solo agua saturada y carbón activado, sin ningún disolvente derivado del petróleo. El grano verde se sumerge en un extracto de café ya sin cafeína, de forma que la cafeína emigra del grano por diferencia de concentración, sin arrastrar consigo los aromas. Es más lento de producir, más caro de comprar, y por eso casi ninguna marca de gran distribución lo usa en sus líneas baratas. A cambio, preserva buena parte de los compuestos responsables del aroma que el método químico aplana por el camino. Si te importa de verdad el descafeinado que bebes, el nombre del proceso impreso en el envase importa más que la marca que lo vende encima."""

MEJOR3 = """Mejor opción número tres. Lavazza ¡Tierra!, la línea sostenible de Lavazza con certificación Rainforest Alliance.

El proyecto Tierra arrancó en 2002 con tres comunidades cafeteras en Honduras, Perú y Colombia, y se amplió en 2010 a productores de Brasil, India y Tanzania. La alianza entre Lavazza y Rainforest Alliance lleva ya más de dos décadas activa, y en 2026 la marca lanzó su primera línea profesional certificada bajo el estándar de agricultura regenerativa de la propia Rainforest Alliance. A diferencia de las diez marcas anteriores, aquí la certificación viene de un organismo externo que audita condiciones sociales y ambientales del cultivo sobre el terreno, no de una promesa de marketing redactada por la propia empresa. Es una marca grande, no un pequeño tostador artesanal, pero es una de las pocas de ese tamaño con más de veinte años de verificación externa real detrás de la palabra "sostenible" impresa en la bolsa."""

MEJOR2 = """Mejor opción número dos. Marcas de café soluble verificadas en laboratorio por Profeco en 2025, dentro del mismo estudio de veintinueve productos, diecinueve de ellos café puro, que ya viste con Golden Hills.

Oro 24 Kilates: cien por cien café puro, con apenas un cero coma dos por ciento de azúcares totales. Altea: cero coma veinte por ciento de azúcares, setenta y nueve miligramos de cafeína por taza, y un tres coma cuatro por ciento de humedad, un dato técnico que garantiza mejor conservación del grano en el tiempo sin apelmazarse ni perder aroma en la lata. El estudio se hizo siguiendo la norma oficial mexicana NMX-F-139, midiendo humedad, acidez, cafeína, presencia de almidón y cumplimiento del etiquetado, no solo el sabor. Son cifras de un organismo público analizando el producto físicamente en laboratorio, buscando azúcar, maíz y garbanzo añadidos, no de la marca describiéndose a sí misma en su propio envase."""

MEJOR1 = """Mejor opción número uno. Juan Valdez. Nacida en 2002, impulsada por la Federación Nacional de Cafeteros de Colombia a través de una empresa creada exactamente para ese fin, Procafecol, con la primera tienda abierta ese mismo año en el aeropuerto El Dorado de Bogotá.

La Federación agrupa hoy a más de quinientas cuarenta mil familias cafeteras colombianas. El modelo de Procafecol se construyó explícitamente sobre franquicias donde los propios caficultores pueden ser dueños del negocio, en vez de vender la marca entera a un grupo extranjero como pasó con casi todas las demás marcas de esta lista.

Cuando compras Juan Valdez, parte de ese dinero vuelve, por diseño del propio modelo de negocio desde el primer día, a quien cultiva el café que estás bebiendo. No a un banquero con activos en tres continentes, como viste en Colcafé. No a una empresa de refrescos de Texas, como viste en Marcilla, Saimaza y L'Or. No a una sala de juntas en Ohio, como viste en Bustelo y Pilón.

Ninguna de estas cinco opciones es perfecta ni está disponible en todos los países a la vez. La diferencia real con las diez anteriores es que aquí la trazabilidad está en el modelo de negocio o en la certificación externa desde el origen, no en un dato que alguien tuvo que investigar durante semanas para encontrar."""

CIERRE = """Antes de volver al súper esta semana, esto es lo que hay que mirar de verdad, en orden.

Uno: si el paquete no dice "tueste natural" de forma explícita y visible, da por hecho que lleva torrefacto, azúcar quemada mezclada con el grano, no café puro. Es obligatorio por ley imprimirlo desde 2012, y casi nadie lo lee antes de pagar en caja.

Dos: si compras descafeinado y el envase no menciona el método de descafeinado, asume que fue con disolvente químico, cloruro de metileno o acetato de etilo, no con agua. La FDA sigue decidiendo qué hacer con ese aditivo desde la petición de diciembre de 2023.

Tres: si la marca suena "tradicional" o "premium" en el eslogan, no des nunca por hecho que es una empresa distinta a la que fabrica la marca barata de al lado en el mismo lineal. Desde agosto de 2025, tres de las marcas más reconocibles de España son, literalmente, la misma compañía estadounidense.

Cuatro: si el envase presume de "sostenible" o "de origen", busca el nombre del organismo externo que lo certifica y desde qué año. Si esa información no está, es una frase de marketing sin nada auditado detrás.

Y cinco: si quieres que tu dinero llegue de verdad a quien cultiva el café, busca modelos declarados desde el origen, como Juan Valdez, no una promesa que alguien tuvo que descubrir después con un vídeo de YouTube.

Diez de las marcas de esta lista pertenecen hoy a un puñado de matrices que ni siquiera coinciden en el sector: una fabrica refrescos de cola en Texas, otra fabrica mermelada en Ohio, otra es el vehículo personal de un banquero con un banco en Londres. Ninguno de esos datos estaba oculto en ningún sitio ilegal. Estaban en comunicados de prensa, registros mercantiles y prensa económica, esperando a que alguien juntara las piezas antes de que entraras al supermercado esta semana."""

SECTIONS = [
    ("HOOK", HOOK),
    ("MARCA 10 - BONKA", MARCA10),
    ("MARCA 9 - MARCILLA", MARCA9),
    ("MARCA 8 - SAIMAZA", MARCA8),
    ("MARCA 7 - HACENDADO", MARCA7),
    ("CTA SUTIL (~35%)", CTA),
    ("MARCA 6 - MARCA BLANCA", MARCA6),
    ("MARCA 5 - NESCAFE", MARCA5),
    ("MARCA 4 - L'OR", MARCA4),
    ("MARCA 3 - BUSTELO Y PILON", MARCA3),
    ("MARCA 2 - COLCAFE", MARCA2),
    ("MARCA 1 - DESCAFEINADO QUIMICO", MARCA1),
    ("MEJORES - INTRO", MEJORES_INTRO),
    ("MEJOR 5 - ESPECIALIDAD", MEJOR5),
    ("MEJOR 4 - SWISS WATER", MEJOR4),
    ("MEJOR 3 - LAVAZZA TIERRA", MEJOR3),
    ("MEJOR 2 - PROFECO MEXICO", MEJOR2),
    ("MEJOR 1 - JUAN VALDEZ", MEJOR1),
    ("CIERRE", CIERRE),
]

if __name__ == "__main__":
    total = sum(len(t.split()) for _, t in SECTIONS)
    cum = 0
    print("Total words:", total, "-> est. minutes @174wpm:", round(total/174, 1))
    for name, t in SECTIONS:
        w = len(t.split())
        cum += w
        print(f"  {name}: {w} words | cumulative {cum} ({round(100*cum/total,1)}%)")
