# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:


define player = Character("[name]")
define oliver = Character("Oliver")
define namine = Character("Naminé")
define naomi = DynamicCharacter("naomi_name")

image Eleanor Idle = "characters/Naomi/EleanorIdle.png"
image EleanorIdle = "EleanorIdle.png"
image Naomi Happy = "characters/Naomi/NaomiFeliz.png"
image phoneItem = "items/phone.png"
image snow park street = "scenarios/SnowParkStreet.jpg"

define audio.childplaying = "sounds/children-playing-pixabay.ogg"

# El juego comienza aquí.

label start:

    $ name = "Rodrigo"
    
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene snow park street
    play sound "sounds/children-playing-pixabay.ogg" loop
    play music "music/Rainbow - fiftysounds.ogg" loop

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    
    # show EleanorIdle at left
    # show player at right

    # Presenta las líneas del diálogo.

    "Durante toda la noche ha estado nevando, y las calles han sido cubiertas por un manto blanco." 
    "El viento, tan frío... El gélido vapor que sale de nuestros labios."
    "Es un indicio de que, ahora sí, el invierno ha llegado."

    "Ya no se escucha el canto de los pájaros, pero sí el suave sonido de la nieve al ser moldeada"
    "Muñecos, ángeles, bolas... Ver a los niños y padres jugar, a los vecinos ayudando a despejar las carreteras..."
    "Hacía tiempo que no sentía esta sensación... Bueno, miento. Desde el año pasado. Sin embargo, queda bien hacerse el interesante de vez en cuando."
    "Cogí aire con fuerza y noté de forma repentina cómo mis pulmones se helaban. Sentía como si una capa de hielo los abrazara lentamente."

    stop music fadeout 1.0
    play sound "sounds/vibrating-phone-pixabay.ogg" loop

    show phoneItem
    "..."
    player "¿Quién me está llamando ahora?"

    stop sound
    play sound "sounds/notification-pixabay.ogg"

    "..."
    play music "music/80s-thrash-metal-track-retro-heavy-metal-energy-pixabay.ogg" loop
    oliver "¡[name], ¿qué haces que todavía no estás aquí?!"
    player "¡¿Oliver?!"
    "Oliver ha sido mi compañero de clase desde el jardín de infancia. Es un chico muy enérgico y se vuelve bastante agresivo cuando la gente llega tarde a los sitios."
    oliver "Tío, ¿no te acuerdas que habíamos quedado para escuchar a Naminé tocar el piano?"
    player "¡Mierda, se me había olvidado!"
    player "(¡El concierto privado de Naminé! ¡¿Cómo se me pudo olvidar?!)"
    player "¡En 10 minutos estoy allí!"
    oliver "Que sean 5, tío. Ya está terminando la segunda pieza."

    stop music fadeout 1.0
    # play sound hangPhone
    # stop sound
    hide phoneItem

    "..."
    "En cuanto colgué el móvil, me dispuse a correr con todas mis fuerzas hacia la casa de Naminé, esquivando semáforos y peatones a mi paso."
    "El viento helaba mi garganta; mis pulmones se congelaban con el aire gélido que respiraba de forma constante y a un ritmo acelerado. Sin embargo, tenía que llegar a tiempo."
    "Tenía que escucharla tocar el piano."

    # play sound catSound

    player "(¿Un gato?)"
    "Efectivamente, vi a un gato balanceándose sobre la carretera y corriendo. Mi instinto me hizo ir rápidamente hacia él."
    "Tenía que rescatarlo. Era mi deber como ciudadano. ¿No es lo que se hace en este tipo de casos?"
    "Cogí al gato mientras veía ese camión intimidante acercándose a nosotros. Me puse de espaldas para protegerlo con mi cuerpo. Notaba cómo ese enorme monstruo de metal estaba a punto de arrollarnos."

    # play sound hornTruck
    # play sound catSound
    # play sound holdClothes

    "De repente, me vi en la acera, a salvo con el felino. Alguien me había agarrado por el cuello del jersey y me había tirado hacia atrás."

    $ naomi_name = "???"

    naomi "Uff, menos mal que llegué a tiempo."
    "Escuché la voz de una chica. Parecía aliviada y alegre al mismo tiempo, aunque también algo exhausta."
    naomi "No pensé que pesaras tanto, pero conseguí agarrarte."
    "Me levanté y me di la vuelta. La chica también estaba sentada en el suelo, tal vez por la inercia. Le ofrecí la mano para ayudarla a levantarse."
    "Ella alzó la vista y aceptó el gesto. Llevaba una chaqueta medio abierta y un gorro de lana, ambos rojos. Pantalones vaqueros comunes y unas deportivas. Sus ojos eran azules, al igual que el mechón de su pelo corto, mayoritariamente negro."
    show Naomi_Happy_PlaceHolder
    naomi "¡Muchas gracias!"
    "Mostró una sonrisa entre dientes. Parecía una chica agradable a simple vista."
    naomi "Deberías tener más cuidado la próxima vez. Bueno, ha sido un placer. ¡Adiós!"
    hide Naomi_Happy_PlaceHolder
    "La misteriosa adolescente se fue inesperadamente rápido, corriendo. Quería agradecerle por rescatarnos a ambos, pero parecía que tenía prisa."
    "El gato me miró y maulló, lamiendo luego mi mano."
    player "(¿Ha sido un placer? Ni siquiera me has dicho tu nombre...)" 
    player "Haa..."
    "Suspiré, intentando calmarme por toda la adrenalina que había experimentado en tan solo un momento. Luego, comencé a reír."
    player "(Es muy atípico ver a personas tan alegres de mi edad. O al menos eso aparenta...)"
    "Dejé al gato en la acera y le di un par de caricias. Saqué el móvil del bolsillo, y la adrenalina que había experimentado anteriormente fue solo un pequeño atisbo de la que me invadió ahora, pensando en Naminé."
    player "(¡Mierda!)"
    "Volví a salir corriendo en dirección a la casa de Naminé, intentando evitar y saltar todos los obstáculos que se me presentaban."

    # Minijuego obstáculos
    # play music minigame

    player "(¡¿Un montón de cajas?!)"

    menu minigames:
        
        "Saltar":
            #play sound boxHit
            "Intenté saltarlas, pero mi empeine rozó la caja más alta del montón y tropecé."
            player "(Argh... ¡Vamos!)"
        "Evitar":
            #play sound dodge
            "Logré esquivarlas fácilmente, pasando solo por un lado."
            player "(Demasiado fácil.)"
            
    label after_minigames:

    player "(¡¿Hielo?!)"

    menu minigames_2:
        
        "Correr":
            #play sound fallGround
            "Intenté correr sobre el hielo, pero me resbalé y caí de culo."
            player "(¡Maldita sea! ¡Levántate!)"
        "Deslizar":
            #play sound ice
            "Salté y me deslicé por el hielo cual pingüino."
            player "(¡Esto tampoco me va a parar!)"
            
    label after_minigames_2:

    player "(¡¿Un cartel sujetado por dos hombres?!)"    

    menu minigames_3:
        
        "Evitar":
            #play sound hitPaper
            "Intenté esquivar a los hombres echándome a un lado, pero no había manera de evitar el cartel. Lo rompí en el acto."
            player "¡Perdón!"
        "Agachar":
            #play sound dodge
            "El cartel estaba lo suficientemente alto como para que pudiera agacharme y pasar por debajo."
            player "(¡Uff, ese sí estuvo cerca!)"
            
    label after_minigames_3:

    # Fin minijuego obstáculos

    # Configurar variables globales tras el minijuego
    
    "Fue un viaje duro, pero logré llegar a la casa de Naminé. Estaba sudando, pero al menos seguía vivo."
    "Corrí hasta su puerta y llamé. Oliver me abrió rápidamente, con una expresión apresurada, pero era demasiado tarde."
    "Cuando llegué al jardín de su casa, solo alcancé a escuchar los acordes finales de la última pieza que ella había planeado tocar."
    player "(Mierda.)"
    "No había otra forma de expresarlo. A pesar de todas las personas que estaban de pie, yo me sentía solo, martirizándome por no haber llegado a tiempo."
    "Este concierto era muy especial para Naminé, pues era su forma de despedirse de sus padres por última vez. Ellos… murieron en un accidente de tráfico hace un mes."
    "La música es la manera en que Naminé se expresa. Los acordes, las notas… son las palabras que usa para mostrar sus sentimientos. El piano… es el idioma con el cual proyecta esas emociones."
    oliver "¡Reacciona, tío!"
    "Sacudí la cabeza brevemente y miré a Oliver con atención. Me había sacado de ese limbo de auto-tortura. Para mí, fueron varios minutos de sufrimiento; para él, solo un segundo efímero en el que me quedé mirando a la nada."
    player "P-perdona, Oliver. ¿Cu-cuándo es la siguiente pieza."
    oliver "¿Siguiente pieza? [name], ella no va a volver a tocar más por hoy..."
    "La respuesta era obvia. Hice la pregunta solo para decir algo, aunque sonara más despistado de lo habitual."
    "O quizá, en el fondo, aún albergaba un atisbo de esperanza de que no hubiera llegado tan tarde… De que tal vez no la había cagado tanto."
    oliver "Venga, al menos salúdala."
    "Oliver, siempre el más optimista del grupo, intentó animarme tras ver mi cara larga. Me dio un par de palmadas en la espalda y juntos nos dirigimos a hablar con ella."
    "Naminé vive en una casa enorme, tanto que solo su jardín trasero es del tamaño de una casa y media como la mía. Había banquetes y globos de colores que combinaban con las hortensias azules del lugar."
    "Hortensias azules… Posiblemente su flor favorita, ya que su madre siempre las cultivaba y cuidaba con esmero."
    "Cuanto más me acercaba a ella, más fuerte me latía el corazón. La ansiedad empezaba a apoderarse de mi cuerpo."
    "Mientras más me acercaba, más podía ver el reflejo dorado de su cabello. Vestía un jersey rojo y, al verme, se levantó del banco para recibirme."
    "Sus ojos color esmeralda me miraban, pero sin el brillo característico de siempre. Sin embargo, a pesar de todo, me recibió con una sonrisa dulce y genuina."
    namine "Buenas, [name]. Qué bueno que al fin hayas venido."
    player "Yo... lo siento mucho... Me distraje un momento y… no me di cuenta del tiempo."
    player "(Tiempo...)"
    "Una palabra que puede tener muchos significados subjetivos, pero que para todos vale lo mismo. Porque el tiempo… no se recupera."
    "Ella simplemente me sonrió y, con delicadeza, sacó de detrás de su mano una hortensia azul para regalármela."
    "La tomé sin entender del todo, pero le devolví la sonrisa. Quería que supiera que, de alguna manera, todo estaba bien."

    # Finaliza el juego:

    return
