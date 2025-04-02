# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:


define mainCharacter = Character("[name]")
define oliver = Character("Oliver")
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
    # show MainCharacter at right

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
    mainCharacter "¿Quién me está llamando ahora?"

    stop sound
    play sound "sounds/notification-pixabay.ogg"

    "..."
    play music "music/80s-thrash-metal-track-retro-heavy-metal-energy-pixabay.ogg" loop
    oliver "¡[name], ¿qué haces que todavía no estás aquí?!"
    mainCharacter "¡¿Oliver?!"
    "Oliver ha sido mi compañero de clase desde el jardín de infancia. Es un chico muy enérgico y se vuelve bastante agresivo cuando la gente llega tarde a los sitios."
    oliver "Tío, ¿no te acuerdas que habíamos quedado para escuchar a Naminé tocar el piano?"
    mainCharacter "¡Mierda, se me había olvidado!"
    mainCharacter "(¡El concierto privado de Naminé! ¡¿Cómo se me pudo olvidar?!)"
    mainCharacter "¡En 10 minutos estoy allí!"
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

    mainCharacter "(¿Un gato?)"
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
    mainCharacter "(¿Ha sido un placer? Ni siquiera me has dicho tu nombre...)" 
    mainCharacter "Haa..."
    "Suspiré, intentando calmarme por toda la adrenalina que había experimentado en tan solo un momento. Luego, comencé a reír."
    mainCharacter "(Es muy atípico ver a personas tan alegres de mi edad. O al menos eso aparenta...)"
    "Dejé al gato en la acera y le di un par de caricias. Saqué el móvil del bolsillo, y la adrenalina que había experimentado anteriormente fue solo un pequeño atisbo de la que me invadió ahora, pensando en Naminé."
    mainCharacter "(¡Mierda!)"
    "Volví a salir corriendo en dirección a la casa de Naminé, intentando evitar y saltar todos los obstáculos que se me presentaban."

    # Minijuego obstáculos
    # play music minigame

    mainCharacter "(¡¿Un montón de cajas?!)"

    menu minigames:
        
        "Saltar":
            #play sound boxHit
            "Intenté saltarlas, pero mi empeine rozó la caja más alta del montón y tropecé."
            mainCharacter "(Argh... ¡Vamos!)"
        "Evitar":
            #play sound dodge
            "Logré esquivarlas fácilmente, pasando solo por un lado."
            mainCharacter "(Demasiado fácil.)"
            
    label after_minigames:

    mainCharacter "(¡¿Hielo?!)"

    menu minigames_2:
        
        "Correr":
            #play sound fallGround
            "Intenté correr sobre el hielo, pero me resbalé y caí de culo."
            mainCharacter "(¡Maldita sea! ¡Levántate!)"
        "Deslizar":
            #play sound ice
            "Salté y me deslicé por el hielo cual pingüino."
            mainCharacter "(¡Esto tampoco me va a parar!)"
            
    label after_minigames_2:

    mainCharacter "(¡¿Un cartel sujetado por dos hombres?!)"    

    menu minigames_3:
        
        "Evitar":
            #play sound hitPaper
            "Intenté esquivar a los hombres echándome a un lado, pero no había manera de evitar el cartel. Lo rompí en el acto."
            mainCharacter "¡Perdón!"
        "Agachar":
            #play sound dodge
            "El cartel estaba lo suficientemente alto como para que pudiera agacharme y pasar por debajo."
            mainCharacter "(¡Uff, ese sí estuvo cerca!)"
            
    label after_minigames_3:

    # Fin minijuego obstáculos
    
    "Fin del minijuego, continúa la historia."

    # Finaliza el juego:

    return
