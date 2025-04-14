# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

#Stats player

define lie = 0
define truth = 0

#Global variables

define callbackNamine = 0

#Others variables

define fails_minigame = 0

#Characters

define player = Character("[name]")
define oliver = Character("Oliver")
define namine = Character("Naminé")
define naomi = DynamicCharacter("naomi_name")
define guest = DynamicCharacter("guest_name")
define guest2 = DynamicCharacter("guest2_name")
define guest3 = DynamicCharacter("guest3_name")

#Images
# https://steamcommunity.com/app/495480/discussions/0/1693785669872968376/
# https://imgur.com/a/GK5QQ

image NaomiDefault = "characters/Naomi/Naomi.png"
image NaomiHappy = "characters/Naomi/NaomiHappy.png"
image NaomiSad = "characters/Naomi/NaomiSad.png"
image NaomiAngry = "characters/Naomi/NaomiAngry.png"
image NaomiSmug1 = "characters/Naomi/NaomiSmug1.png"
image NaomiSmug2 = "characters/Naomi/NaomiSmug2.png"

image NamineDefault = "characters/Namine/Namine.png"
image NamineHappy = "characters/Namine/NamineHappy.png"
image NamineSad = "characters/Namine/NamineSad.png"
image NamineAngry = "characters/Namine/NamineAngry.png"

image phoneItem = "items/phone.png"
image snow park street = "backgrounds/SnowParkStreet.png"
image street snow 1 = "backgrounds/Street-snow.png"
image street snow 6 = "backgrounds/Street-snow6.png"
image street minigames = "backgrounds/Street-snow2.png"
image center town = "backgrounds/Street-snow8.png"
image namine house = "backgrounds/Naminehouse.png"
image namine garden = "backgrounds/Naminegarden.png"

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

    scene image "backgrounds/Cat.png"
    play sound "sounds/cat-meow.ogg"

    player "(¿Un gato?)"
    "Efectivamente, vi a un gato balanceándose sobre la carretera y corriendo. Mi instinto me hizo ir rápidamente hacia él."
    "Tenía que rescatarlo. Era mi deber como ciudadano. ¿No es lo que se hace en este tipo de casos?"

    play sound "sounds/truck-signal.ogg"
    
    "Cogí al gato mientras veía ese camión intimidante acercándose a nosotros. Me puse de espaldas para protegerlo con mi cuerpo. Notaba cómo ese enorme monstruo de metal estaba a punto de arrollarnos."

    scene street snow 1
    play sound "sounds/grab-clothes.ogg"

    "De repente, me vi en la acera, a salvo con el felino. Alguien me había agarrado por el cuello del jersey y me había tirado hacia atrás."

    $ naomi_name = "???"

    naomi "Uff, menos mal que llegué a tiempo."
    "Escuché la voz de una chica. Parecía aliviada y alegre al mismo tiempo, aunque también algo exhausta."
    naomi "No pensé que pesaras tanto, pero conseguí agarrarte."
    "Me levanté y me di la vuelta. La chica también estaba sentada en el suelo, tal vez por la inercia. Le ofrecí la mano para ayudarla a levantarse."
    "Ella alzó la vista y aceptó el gesto. Llevaba una chaqueta medio abierta y un gorro de lana, ambos rojos. Pantalones vaqueros comunes y unas deportivas. Sus ojos eran azules, al igual que el mechón de su pelo corto, mayoritariamente negro."
    show NaomiHappy
    naomi "¡Muchas gracias!"
    "Mostró una sonrisa entre dientes. Parecía una chica agradable a simple vista."
    naomi "Deberías tener más cuidado la próxima vez. Bueno, ha sido un placer. ¡Adiós!"
    hide NaomiHappy
    "La misteriosa adolescente se fue inesperadamente rápido, corriendo. Quería agradecerle por rescatarnos a ambos, pero parecía que tenía prisa."
    "El gato me miró y maulló, lamiendo luego mi mano."
    player "(¿Ha sido un placer? Ni siquiera me has dicho tu nombre...)" 
    player "Ahh..."
    "Suspiré, intentando calmarme por toda la adrenalina que había experimentado en tan solo un momento. Luego, comencé a reír."
    player "(Es muy atípico ver a personas tan alegres de mi edad. O al menos eso aparenta...)"
    "Dejé al gato en la acera y le di un par de caricias. Saqué el móvil del bolsillo, y la adrenalina que había experimentado anteriormente fue solo un pequeño atisbo de la que me invadió ahora, pensando en Naminé."
    player "(¡Mierda!)"
    "Volví a salir corriendo en dirección a la casa de Naminé, intentando evitar y saltar todos los obstáculos que se me presentaban."

    # Minijuego obstáculos

    scene street minigames
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
    
    scene namine house

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
    show NamineDefault
    namine "Buenas, [name]. Qué bien que al fin hayas venido."
    player "Yo... lo siento mucho... Me distraje un momento y… no me di cuenta del tiempo."
    hide NamineDefault
    player "(Tiempo...)"
    "Una palabra que puede tener muchos significados subjetivos, pero que para todos vale lo mismo. El tiempo… no se recupera."
    show NamineHappy
    "Ella simplemente me sonrió y, con delicadeza, sacó de detrás de su mano una flor. Simplemente me la dio."
    "La tomé sin entender del todo, pero le devolví la sonrisa. Ella quería que supiera que, de alguna manera, todo estaba bien."
    player "(¿Una flor viva... en esta época del año?)"
    "No le pregunté, solamente la guardé dentro de mi chaqueta sin pedir explicaciones sobre la flor."
    hide NamineHappy
    show NamineDefault at right
    show Oliver_PlaceHolder at left
    oliver "Bueno, no nos quedemos aquí. Vamos a almorzar algo, ¿no?"
    namine "Sí, tenemos un montón de comida en el banquete. Puedes coger lo que te apetezca."
    hide NamineDefault
    hide Oliver_PlaceHolder

    scene namine garden

    "Miré hacia la mesa y vi que, posiblemente, contenía toda la pirámide alimenticia que alguna vez observé en los carteles de los pediatras cuando era niño."
    "Desde mocktails refinados y mini tartitas de queso brie con mermelada de higos, hasta costillas de cordero con costra de pistachos y puré de zanahoria."
    player "(¡Pero si esto no es un almuerzo, es un festín!)"
    show NamineDefault at right
    show Oliver_PlaceHolder at left
    oliver "¿Y esa cara. [name]? ¡Se te está cayendo la baba!"
    "Los tres empezamos a reír por su comentario mientras nos dirigíamos a comer."
    "Al llegar, como todo era libre, comenzamos a picotear lo que veíamos. Yo fui directo a los postres y cogí una tarta de queso con mermelada y nata."
    oliver "¿Ese va a ser tu estupendo almuerzo?"
    player "¿Y lo malo?"
    oliver "No sé, estamos en invierno ¿sabes?"
    player "Mejor, así no se derrite."

    if fails_minigame == 3:
        hide NamineDefault
        hide Oliver_PlaceHolder
        show NamineHappy
        namine "Es una gran manera de recuperar energía. Parece que el camino hasta aquí te ha supuesto un problema."
        "Me dijo con una sonrisa mientras sacaba su pañuelo y empezaba a quitarme suciedad de la cara, a la vez que me sacudía el pelo lleno de nieve."
    elif fails_minigame >= 1 and fails_minigame < 3:
        hide NamineDefault
        hide Oliver_PlaceHolder
        show NamineHappy
        namine "Es una gran manera de recuperar energía. Te noto un poco con el pelo blanco"
        "Al parecer, se dio cuenta de todas las caídas que tuve hasta venir aquí. Me sentí algo avergonzado, aunque ella simplemente sonrió."
    else:
        hide NamineDefault
        oliver "Bueno, me sorprende que hayas llegado de una pieza. Con el hambre que tienes y lo rojo que estas, seguro hiciste un buen maratón."

    hide NamineDefault
    hide NamineHappy
    hide Oliver_PlaceHolder
    "Justo cuando estaba terminando de comer mi tarta, vi la cabeza de la chica de antes asomándose en el jardín. Rápidamente, dejé el plato en la mesa y fui dentro de la casa para salir corriendo a la calle."
    show Oliver_PlaceHolder
    oliver "¡Eh! ¡¿pero a dónde vas?!"  
    hide Oliver_PlaceHolder
    "Llegué afuera y la vi huir, doblando la esquina."

    menu prologue:
        
        "Correr":
            # play sound correr
            scene street snow 6
            "Fui rápidamente a girar esa misma esquina para perseguirla. No podía perderla de vista."
            player "¡Eh, espera!"
            "La chica parecía ignorarme, corriendo con todas sus fuerzas, intentando evitarme. Nos estábamos acercando cada vez más a zonas más transitadas, concretamente la plaza."
            "Ella no paraba de dar giros bruscos para poder perderme. Sin embargo, en este punto yo no podía permitirme parar."

            scene center town
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

            show NaomiHappy
            naomi "Nos volvemos a ver."
            "Sacudí la cabeza para que así mi rostro volviese a relajarse. Seguídamente, bajé un poco la cabeza, rascándome la nuca, reflejando así mi pequeña timidez en aquel preciso momento."
            player "Ho-hola... no... me dijiste tu nombre la última vez."
            "La chica simplemente sonrió antes de responderme."
            hide NaomiHappy
            show NaomiDefault
            naomi "Naomi, mi nombre es Naomi."

            $ naomi_name = "Naomi"

            player "Así que Naomi... ¡Encantado de conocerte! Yo... me llamo [name]"
            naomi "Un placer, [name]. Y... por cierto... parece que te están buscando."
            player "¿Hmm?"
            hide NaomiDefault
            "Unos policías se dirigían hacia mí. Por lo que se veía en su rostro parecía que no venían de buenas."
            "Atrás de ellos salió luego otra persona, una chica que vestía de forma muy parecida a Naomi, señalándome muy enfurecida."
            player "(¡No me digas que estaba persiguiendo a otra persona!)"

            $ guest_name = "Policía"
            $ guest2_name = "Chica"

            guest "¡Eh tú! Será mejor que vengas a darnos una explicación"
            "Los policías se acercaron con la chica. Yo, por obvias razones, no moví ni un solo músculo de mis pies."
            guest "Esta chica ha dicho que llevas bastante minutos corriendo detrás de ella. ¿No es así?"
            "El policía buscaba la confirmación de la chica. Ella asintió un par de veces antes de responder, mientras fruncía el ceño de forma malhumorada."
            guest2 "Así es agente. ¡Me lleva persiguiendo como siete manzanas antes de llegar a la plaza!"
            menu lietrue:
                "Mentir":
                    $ lie += 1
                    player "¡E-eso es mentira! Simplemente tenía prisa para llegar a la plaza y no perderme los descuentos de ahora..."
                    guest2 "¡Pero si cogí un desvío para evitarte! ¡Hubieras llegado antes por otro camino!"
                    player "(¡Mierda!)"
                    "De repente, noté como alguien me abrazó el brazo izquierdo. Al girar mi rostro, vi a Naomi, sujetando una bolsa de castañas calientes."
                    naomi "¡Viene conmigo agente! Habíamos quedado para tomar algo y comprar algunas cosas de oferta."
                "Decir la verdad":
                    $ truth += 1
                    player "¡La confundí con otra chica que viste muy parecida a ella!"
                    guest2 "Sí, claro... ¿quién?"
                    "Al señalar donde estaba Naomi ya no había nadie. Empecé a sudar mientras mi músculos comenzaban también a temblar."
                    player "(¿Dónde coño ha ido?)"
                    "Los policías reflejaban un rostro dubitativo mientras me cogían del brazo rápidamente."
                    "De repente, Naomi apareció agarrándome el otro brazo, tirando de él suavemente. Mientras sujetaba una bolsa de castañas calientes."
                    naomi "¡Perdonen agentes! ¡Viene conmigo! Había ido un momento a comprar algo para comer."
            label lietrue:

            "Los policías se fijaron en Naomi y luego en la otra chica. Pudieron deducir que se parecían bastante en la ropa que llevaban."
            guest2 "A-ah... pero llevabas la m-misma ro-"
            naomi "¿Pasa algo?"
            "Naomi arqueó una ceja a la chica, extrañada. Desde mi punto de vista, podía ver claramente como una de sus comisuras temblaban, intentando aguantar la compostura y no reirse de la situación. Parecía que se estaba divirtiendo."
            guest "Bueno, parece que todo ha sido un mal entendido. Lo siento mucho muchachos, disfrutad del paseo."
            "La desconocida no sabía que decir, simplemente suspiró pesadamente y se disculpó. A partir de ahí, simplemente siguió su camino por la plaza."
            "Miré a Naomi a la vez que ella hizo lo mismo conmigo. Ambos empezamos a sonreir intentando aguantar la carcajada, pero que inevitablemente salió. El momento era demasiado subrealista como para no liberar todos los nervios de golpe."
            "Ella sonrió y extendió la bolsa de castañas para que cogiese una."
            player "Gracias, no solo por las castañas, también por librarme de una buena."
            naomi "Te vi un poco en apuros desde lejos, así que vine a ver que pasa."
            player "Literalmente... me has salvado dos veces hoy. ¿Cómo es posible que hayas aparecido esas dos veces para ayudarme?"
            naomi "Podría decirse que soy una especie de súper heroína. O... tu ángel de la guarda"
            "Al decir esas últimas palabras mis mejillas empezaron a ruborizarse."
            naomi "Vaya... parece que estás cogiendo frío."
            player "N-no te preocupes. Estoy bien realmente, habrá sido de correr antes al ver hasta aquí."
            naomi "Está bien. Toma, puede quedarte el resto."
            "Naomi me ofreció lo que quedaba de castañas con una sonrisa, para luego darse la vuelta y alzar su brazo izquierdo para despedirse alegremente."
            naomi "¡Hasta otra, [name]!"
            "Le devolví la sonrisa mientras también me despedía de ella alzando mi diestra. Tras ello empecé a comer las castañas a la vez que salía de la plaza dirigiéndome de nuevo a casa de Naminé."

            "Tras pasear por las calles y acabarme las castañas, empecé a desperazarme estirando los brazos hacia arriba. Seguidamente busqué el móvil por los bolsillo de mi chaqueta, y ahí fue cuando noté que la flor que me dio Naminé no estaba."
            player "(No... ¡No puede ser!)"
            "Entré en pánico y me puse buscar por todos los lados donde había pasado para buscar la flor. Pero todo se volvió más difícil de buscar cuando volvió a nevar."
            "Las calles cada vez estaban más cubiertas de nieve que antes. Todo lo que hubiese en el suelo posiblemente ya había sido tapado, pero aún así... yo seguía apartando la nieve, quemándome las manos por el frío. Con la esperanza de encontrar esa flor."
            "Me levanté y la noche ya había caído. Las farolas se encendían poco a poco, y yo... simplemente me quité la nieve que podía de la cabeza, para luego dirigirme a mi casa cabizbajo."
            "Cogí el móvil y empecé a revisarlo. Tenía las notificaciones en silencio, así que no me di cuenta de todos los mensajes que me habían mandado hasta entonces."
            "Oliver y Naminé estaban preocupados por mí."
            player "Ahh..."
            "Suspiré mientras guardaba el móvil mientras pensaba en como dejé de nuevo a mis amigos tirados."
            "No escuché a Naminé tocar el piano."
            "No me quedé con ella el resto el día."
            "No hice que supiera de mí en todo el día."
            "Perdí el único regalo que me hizo hoy."
            player "(Soy un completo desastre.)"
            player "(¿Debería llamarla?)"

            menu callback:
                "Llamarla":
                    $ collbackNamine += 1
                    "El número se quedaría comunicando."
                    player "Ah..."
                    player "(Se habrá quedado dormida. Es tarde ya.)"
                "No llamarla":
                    player "(Seguramente esté durmiendo. Será mejor no molestarla.)"
            label callback:

            player "(Es hora de irse a casa, [name])"
            "Caminé un largo tiempo, por dar un paseo lento, hasta llegar a mi casa."
            "Tras volver mis padres ya se habían acostado. Me habían dejado la cena caliente dentro del microondas, así que la saqué para comer mientras cogía el móvil para ver a que hora había llegado."
            player "(Las diez...)"
            "La una de la noche."
            "Tardé unas dos horas en llegar a casa al ritmo desanimado con el que andaba. Pero me pasé más tiempo intentando encontrar el regalo de Naminé, unas tres o cuatro horas dando vueltas."
            "Dejé media comida en la mesa. No tenía un humor muy alto como para tener el estómago realmente vacío. Tiré lo que quedaba, eché el plato en el fregadero, y me fui directamente a la cama."
            "Solamente quería cerrar los ojos, descansar y dejar de pensar. Pero el día se repetía una y otra vez en mi mente. Oliver... el regalo... Naminé... el gato... Naomi..."
            player ("Naomi...")
            "Pensaba si mañana la volvería a ver una vez más."
        "Quedarse":
            play sound "sounds/ice-slide.ogg"
            "Salté y me deslicé por el hielo cual pingüino."
            player "(¡Esto tampoco me va a parar!)"
            
    label after_prologue:       

    # Finaliza el juego:

    return