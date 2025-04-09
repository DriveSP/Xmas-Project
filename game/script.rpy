# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Variables

define fails_minigame = 0

#Characters

define player = Character("[name]")
define oliver = Character("Oliver")
define namine = Character("Naminé")
define naomi = DynamicCharacter("naomi_name")
define guest = DynamicCharacter("guest_name")

#Images
# https://steamcommunity.com/app/495480/discussions/0/1693785669872968376/
# https://imgur.com/a/GK5QQ
image Eleanor Idle = "characters/Naomi/EleanorIdle.png"
image EleanorIdle = "EleanorIdle.png"
image Naomi Happy = "characters/Naomi/NaomiFeliz.png"
image phoneItem = "items/phone.png"
image snow park street = "scenarios/SnowParkStreet.jpg"

#Sounds

define audio.phone = "sounds/vibrating-phone.ogg"
define audio.notification = "sounds/notification.ogg"
define audio.hangup = "sounds/cell-phone-hang-up.ogg"
define audio.meow = "sounds/cat-meow.ogg"
define audio.dodge = "sounds/dodge.ogg"
#define audio.run = "sounds/"

# El juego comienza aquí.

label start:

    $ name = "Rodrigo"
    
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene snow park street
    play sound "sounds/children-playing.ogg" loop
    play music "music/Rainbow - fiftysounds.ogg" loop

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.

    "Durante toda la noche ha estado nevando, y las calles han sido cubiertas por un manto blanco." 
    "El viento, tan frío... El gélido vapor que sale de nuestros labios."
    "Es un indicio de que, ahora sí, el invierno ha llegado."

    "Ya no se escucha el canto de los pájaros, pero sí el suave sonido de la nieve al ser moldeada"
    "Muñecos, ángeles, bolas... Ver a los niños y padres jugar, a los vecinos ayudando a despejar las carreteras..."
    "Hacía tiempo que no sentía esta sensación... Bueno, miento. Desde el año pasado. Sin embargo, queda bien hacerse el interesante de vez en cuando."
    "Cogí aire con fuerza y noté de forma repentina cómo mis pulmones se helaban. Sentía como si una capa de hielo los abrazara lentamente."

    stop music fadeout 1.0
    play sound phone loop

    show phoneItem
    "..."
    player "(¿Quién me está llamando ahora?)"

    stop sound
    play sound notification

    "..."
    play music "music/Push - Alex Productions.ogg" loop
    oliver "¡[name], ¿qué haces que todavía no estás aquí?!"
    player "¡¿Oliver?!"
    "Oliver ha sido mi compañero de clase desde el jardín de infancia. Es un chico muy enérgico y se vuelve bastante agresivo cuando la gente llega tarde a los sitios."
    oliver "Tío, ¿no te acuerdas que habíamos quedado para escuchar a Naminé tocar el piano?"
    player "¡Mierda, se me había olvidado!"
    player "(¡El concierto privado de Naminé! ¡¿Cómo se me pudo olvidar?!)"
    player "¡En 10 minutos estoy allí!"
    oliver "Que sean 5, tío. Ya está terminando la segunda pieza."

    stop music fadeout 1.0
    play sound hangup
    hide phoneItem

    "..."
    "En cuanto colgué el móvil, me dispuse a correr con todas mis fuerzas hacia la casa de Naminé, esquivando semáforos y peatones a mi paso."
    "El viento helaba mi garganta; mis pulmones se congelaban con el aire frío que respiraba de forma constante y a un ritmo acelerado. Sin embargo, tenía que llegar a tiempo."
    "Tenía que escucharla tocar el piano."

    play sound "sounds/cat-meow.ogg"

    player "(¿Un gato?)"
    "Efectivamente, vi a un gato balanceándose sobre la carretera y corriendo. Mi instinto me hizo ir rápidamente hacia él."
    "Tenía que rescatarlo. Era mi deber como ciudadano. ¿No es lo que se hace en este tipo de casos?"

    play sound "sounds/truck-signal.ogg"
    
    "Cogí al gato mientras veía ese camión intimidante acercándose a nosotros. Me puse de espaldas para protegerlo con mi cuerpo. Notaba cómo ese enorme monstruo de metal estaba a punto de arrollarnos."

    play sound "sounds/grab-clothes.ogg"

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
    play music "music/Jingle Bells - Mystery Mammal.ogg" loop

    player "(¡¿Un montón de cajas?!)"

    menu minigames:
        
        "Saltar":
            play sound "sounds/box-crash.ogg"
            "Intenté saltarlas, pero mi empeine rozó la caja más alta del montón y tropecé."
            player "(Argh... ¡Vamos!)"
            $ fails_minigame += 1
        "Evitar":
            play sound dodge
            "Logré esquivarlas fácilmente, pasando solo por un lado."
            player "(Demasiado fácil.)"
            
    label after_minigames:

    player "(¡¿Hielo?!)"

    menu minigames_2:
        
        "Correr":
            play sound "sounds/body-fall.ogg"
            "Intenté correr sobre el hielo, pero me resbalé y caí de culo."
            player "(¡Maldita sea! ¡Levántate!)"
            $ fails_minigame += 1
        "Deslizar":
            play sound "sounds/ice-slide.ogg"
            "Salté y me deslicé por el hielo cual pingüino."
            player "(¡Esto tampoco me va a parar!)"
            
    label after_minigames_2:

    player "(¡¿Un cartel sujetado por dos hombres?!)"    

    menu minigames_3:
        
        "Agachar":
            play sound dodge
            "El cartel estaba lo suficientemente alto como para que pudiera agacharme y pasar por debajo."
            player "(¡Uff, ese sí estuvo cerca!)"
        "Evitar":
            play sound "sounds/paper-crash.ogg"
            "Intenté esquivar a los hombres echándome a un lado, pero no había manera de evitar el cartel. Lo rompí en el acto."
            player "¡Perdón!"
            $ fails_minigame += 1
            
    label after_minigames_3:

    stop music fadeout 1.0   
    # Fin minijuego obstáculos

    # Configurar variables globales tras el minijuego
    
    "Fue un viaje duro, pero logré llegar a la casa de Naminé. Estaba sudando, pero al menos seguía vivo."
    "Corrí hasta su puerta y llamé. Oliver me abrió rápidamente, con una expresión apresurada."
    show Oliver_PlaceHolder
    oliver "¡Vamos! ¡Corre!"
    hide Oliver_PlaceHolder
    "Pero era demasiado tarde..."
    "Cuando llegué al jardín de su casa, solo alcancé a escuchar los acordes finales de la última pieza que ella había planeado tocar."
    player "(Mierda.)"
    "No había otra forma de expresarlo. A pesar de todas las personas que estaban de pie, yo me sentía solo, martirizándome por no haber llegado a tiempo."
    "Este concierto significaba mucho para Naminé. Era su forma de despedirse de sus padres por última vez. Ellos… murieron en un accidente de tráfico hace un mes."
    "La música es la manera en que Naminé se expresa. Los acordes, las notas… son las palabras que usa para mostrar sus sentimientos. El piano… es el idioma con el cual proyecta esas emociones."
    show Oliver_PlaceHolder
    oliver "¡Reacciona, tío!"
    "Sacudí la cabeza brevemente y miré a Oliver con atención. Me había sacado de ese limbo de autotortura. Para mí, fueron varios minutos de sufrimiento; para él, solo un segundo efímero en el que me quedé mirando a la nada."
    player "P-perdona, Oliver. ¿C-cuándo es la siguiente pieza?"
    oliver "¿Siguiente pieza? [name], ella no va a volver a tocar más por hoy..."
    "La respuesta era obvia. Hice la pregunta solo para decir algo, aunque sonara más despistado de lo habitual."
    "O quizá, en el fondo, aún albergaba un atisbo de esperanza de que no hubiera llegado tan tarde… De que tal vez no la había cagado tanto."
    oliver "Venga, al menos salúdala."
    "Oliver, siempre el más optimista del grupo, intentó animarme tras ver mi cara larga. Me dio un par de palmadas en la espalda y juntos nos dirigimos a hablar con ella."
    hide Oliver_PlaceHolder
    "Naminé vive en una casa enorme, tanto que solo su jardín trasero es del tamaño de una casa y media como la mía. Había banquetes y globos de colores que combinaban con el blanco de la nieve que tapaba las hierbas."
    "Su jardín se vuelve triste en invierno, ya que las flores que siempre nacen pierden su color por culpa de los días gélidos."
    player "(Este jardín se ve triste ahora mismo… sobre todo sin aquellas extrañas flores que plantaba su madre.)" 
    "Posiblemente el tipo de flor más especial del jardín, ya que su madre siempre las cultivaba y cuidaba con esmero."
    "Cuanto más me acercaba a ella, más fuerte me latía el corazón. La ansiedad empezaba a apoderarse de mi cuerpo."
    "Mientras más me aproximaba, más podía ver el reflejo dorado de su cabello. Llevaba puesto un jersey rojo y pantalones vaqueros cortos junto a unas medias térmicas."
    "Ella se levantó del banco, y al verme, vino a recibirme."
    "Sus ojos color esmeralda me miraban, pero sin el brillo característico de siempre. Sin embargo, a pesar de todo, me recibió con una sonrisa dulce y genuina."
    show Namine_PlaceHolder
    namine "Buenas, [name]. Qué bien que al fin hayas venido."
    player "Yo... lo siento mucho... Me distraje un momento y… no me di cuenta del tiempo."
    hide Namine_PlaceHolder
    player "(Tiempo...)"
    "Una palabra que puede tener muchos significados subjetivos, pero que para todos vale lo mismo. El tiempo… no se recupera."
    show Namine_Happy_PlaceHolder
    "Ella simplemente me sonrió y, con delicadeza, sacó de detrás de su mano una flor. Simplemente me la dio."
    "La tomé sin entender del todo, pero le devolví la sonrisa. Ella quería que supiera que, de alguna manera, todo estaba bien."
    player "(¿Una flor viva... en esta época del año?)"
    "No le pregunté, solamente la guardé dentro de mi chaqueta sin pedir explicaciones sobre la flor."
    hide Namine_Happy_PlaceHolder
    show Namine_PlaceHolder at right
    show Oliver_PlaceHolder at left
    oliver "Bueno, no nos quedemos aquí. Vamos a almorzar algo, ¿no?"
    namine "Sí, tenemos un montón de comida en el banquete. Puedes coger lo que te apetezca."
    hide Namine_PlaceHolder
    hide Oliver_PlaceHolder
    "Miré hacia la mesa y vi que, posiblemente, contenía toda la pirámide alimenticia que alguna vez observé en los carteles de los pediatras cuando era niño."
    "Desde mocktails refinados y mini tartitas de queso brie con mermelada de higos, hasta costillas de cordero con costra de pistachos y puré de zanahoria."
    player "(¡Pero si esto no es un almuerzo, es un festín!)"
    show Namine_PlaceHolder at right
    show Oliver_PlaceHolder at left
    oliver "¿Y esa cara. [name]? ¡Se te está cayendo la baba!"
    "Los tres empezamos a reír por su comentario mientras nos dirigíamos a comer."
    "Al llegar, como todo era libre, comenzamos a picotear lo que veíamos. Yo fui directo a los postres y cogí una tarta de queso con mermelada y nata."
    oliver "¿Ese va a ser tu estupendo almuerzo?"
    player "¿Y lo malo?"
    oliver "No sé, estamos en invierno ¿sabes?"
    player "Mejor, así no se derrite."

    if fails_minigame == 3:
        hide Namine_PlaceHolder
        hide Oliver_PlaceHolder
        show Namine_Happy_PlaceHolder
        namine "Es una gran manera de recuperar energía. Parece que el camino hasta aquí te ha supuesto un problema."
        "Me dijo con una sonrisa mientras sacaba su pañuelo y empezaba a quitarme suciedad de la cara, a la vez que me sacudía el pelo lleno de nieve."
    elif fails_minigame >= 1 and fails_minigame < 3:
        hide Namine_PlaceHolder
        hide Oliver_PlaceHolder
        show Namine_Happy_PlaceHolder
        namine "Es una gran manera de recuperar energía. Te noto un poco con el pelo blanco"
        "Al parecer, se dio cuenta de todas las caídas que tuve hasta venir aquí. Me sentí algo avergonzado, aunque ella simplemente sonrió."
    else:
        hide Namine_PlaceHolder
        oliver "Bueno, me sorprende que hayas llegado de una pieza. Con el hambre que tienes y lo rojo que estas, seguro hiciste un buen maratón."

    hide Namine_PlaceHolder
    hide Namine_Happy_PlaceHolder
    hide Oliver_PlaceHolder
    "Justo cuando estaba terminando de comer mi tarta, vi la cabeza de la chica de antes asomándose en el jardín. Rápidamente, dejé el plato en la mesa y fui dentro de la casa para salir corriendo a la calle."
    show Oliver_PlaceHolder
    oliver "¡Eh! ¡¿pero a dónde vas?!"  
    hide Oliver_PlaceHolder
    "Llegué afuera y la vi huir, doblando la esquina."

    menu prologue:
        
        "Correr":
            # play sound correr
            "Fui rápidamente a girar esa misma esquina para perseguirla. No podía perderla de vista."
            player "¡Eh, espera!"
            "La chica parecía ignorarme, corriendo con todas sus fuerzas, intentando evitarme. Nos estábamos acercando cada vez más a zonas más transitadas, concretamente la plaza."
            "Ella no paraba de dar giros bruscos para poder perderme. Sin embargo, en este punto yo no podía permitirme parar."
            "Al entrar en la plaza, todo estaba lleno de puestos de mercado, por lo que la perdí de vista en un santiamén."
            "Me detuve a descansar un poco y continué caminando a paso lento, mirando hacia todos lados, pero volví a perderla de vista..."
            "Dándome por vencido, me dispuse a sentarme cerca de una fuente. Allí pude ver varios niños correteando y jugando. Poco a poco una sonrisa invadía mi rostro, viendo la genuidad e inocencia de aquellos chicos."
            "A pesar de ello, uno de los niños estaba siendo demasiado agresivo, empujando a uno por su rabieta. Justo detrás de ese chico había un escalón algo elevado, apuntando a la altura perfecta para encontrarse con la nuca del muchacho."
            "Mis pupilas se encogieron. Me levanté rápidamente, alzando el brazo mientras corría hacia el chico. Sin embargo, vi como una sombra se movía ligeramente por el espacio, parecía casi inhumano."
            "La silueta negra atrapó al niño en brazos antes de que cayera y, cuando volví a parpadear, esa oscura figura se convirtió en la chica que estaba buscando..."
            "Me detuve en seco, paralizado, viendo cómo aquella misteriosa chica sostenía al chico."

            $ guest_name = "Niño"

            guest "¡Ay, gracias señorita!"
            naomi "Ten más cuidado la próxima vez, ¿vale?"
            guest "¡Sí! ¡Hasta otra!"

            "El niño volvió con el grupo como si nada hubiese pasado. Aquel chico aún no era consciente de que su vida pendía de un hilo hace tan solo unos segundos."
            "La chica se levantó y me miró con una sonrisa."

            show Naomi_Happy_PlaceHolder
            naomi "Nos volvemos a ver."
            "Sacudí la cabeza para que así mi rostro volviese a relajarse. Seguídamente, bajé un poco la cabeza, rascándome la nuca, reflejando así mi pequeña timidez en aquel preciso momento."
            player "Ho-hola... no... me dijiste tu nombre la última vez."
            "La chica simplemente sonrió antes de responderme."
            hide Naomi_Happy_PlaceHolder
            show Naomi_PlaceHolder
            naomi "Naomi, mi nombre es Naomi."

            $ naomi_name = "Naomi"

            player "Así que Naomi... ¡Encantado de conocerte! Yo... me llamo [name]"
            naomi "Un placer, [name]. Y... por cierto... parece que te están buscando."
            player "¿Hmm?"
            hide Naomi_PlaceHolder
            "Unos policías se dirigían hacia mí. Por lo que se veía en su rostro parecía que no venían de buenas."
            "Atrás de ellos salió luego otra persona, una chica que vestía de forma muy parecida a Naomi, señalándome muy enfurecida."
            player "(¡No me digas que estaba persiguiendo a otra persona!)"


        "Quedarse":
            play sound "sounds/ice-slide.ogg"
            "Salté y me deslicé por el hielo cual pingüino."
            player "(¡Esto tampoco me va a parar!)"
            
    label after_prologue:       

    # Finaliza el juego:

    return