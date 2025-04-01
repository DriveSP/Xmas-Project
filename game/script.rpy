# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:


define mainCharacter = Character("[name]")
define oliver = Character("Oliver")

image EleanorIdle = "EleanorIdle.png"
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

    "Durante toda la noche ha estado nevando, y las calles  fueron cubiertas en un manto blanco." 
    "El viento tan frío, el gélido vapor que salen de nuestro labios."
    "Un indicio de que, ahora sí, el invierno ha llegado."

    "Ya no se escucha el canto de los pájaros, pero sí el suave sonido de la nieve siendo moldeada."
    "Muñecos, ángeles, bolas... Ver a los niños y padres jugar, vecinos ayudando a despejar las carreteras..."
    "Hacía tiempo que no sentía esta sensación... Bueno, miento. Desde el año pasado. Sin embargo, queda bien hacerse el interesante de vez en cuando."
    "Cogí aire con fuerza y noté de forma repentina como mis pulmones se helaban. Sentía como si una capa de hielo abrazara mis pulmones lentamente."

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
    "Oliver ha sido mi compañero de clases desde el jardín de infancia. Es una chico muy energético, se vuelve muy agresivo cuando la gente llega tarde a los sitios."
    oliver "Tío, ¿no te acuerdas que habíamos quedado para escuchar a Naminé tocar el piano?"
    mainCharacter "¡Mierda, se me había olvidado!"
    "¡El concierto privado de Naminé, ¿cómo se me pudo olvidar?!"
    mainCharacter "¡En 10 minutos estoy allí!"
    oliver "Que sean 5 tío, ya está terminando la segunda pieza."

    stop music fadeout 1.0
    # play sound hang phone
    # stop sound

    "..."
    "En cuanto colgué el móvil me dispuse a correr con todas mis fuerzas hacia la casa de Naminé. Evadiendo todos los semáforos y peatones que veía en mi camino."
    "El viento helaba mi garganta, mis pulmones se congelaban con el aire gélido que respiraba de forma constante y a un ritmo acelerador. Sin embargo, tenía que llegar a tiempo."
    "Tenía que escucharla tocar el piano."

    # Finaliza el juego:

    return
