# Вы можете расположить сценарий своей игры в этом файле.
init python:
    res = False

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define v = Character('Автор', color="#ffe4c4")
define a = Character('[input_name]', color="#c8ffc8")
define b = Character('Мысли [input_name]а', color="#ffe4c4")
define w = Character('Медсестра', color="#ffe4c4")
define gm = Character('Старуха', color='#c8ffc8')

# Переменные
define banan = False
define next_stage = 0
define next_stage_v1 = 0

# Игра начинается здесь:
label start:
    play sound "рсэ.mp3" volume 0.02 if_changed
    $ true_v1 = 0
    scene bg
    "Я очнулся в непонятной для меня комнате." 
    "Как я сюда попал?\nИ почему я не могу вспомнить ни одной детали своей жизни"
    "Я с трудом решился встать и осмотреть комнату"

    show agrgg:
        xalign 0.9
        yalign -0.1

    "Комната была маленькая, с одним окном, через которое проникало бледное утреннее солнце." with dissolve
    "Все в этом месте казалось мне незнакомым, и я чувствовал себя как в чужом мире."
    "Неожиданно я услышал шаги, доносящиеся из-за двери."
    v "{cps=25}Дверь открывается и в комнату входит девушка{/cps}"
    show surgg:
        xalign 0.9
        yalign -0.1

    show vg:
        xalign 0.2
        yalign -0.5
        xzoom 0.7
        yzoom 0.7

    e "{cps=25}Привет, я Эйлин{/cps}" with dissolve
    
    $ input_name = renpy.input("Какое твоё имя?")

    a "{cps=25}Меня зовут [input_name]{/cps}"

    e "{cps=25}[input_name], я нашла тебя на улице и решила привезти сюда.\nТы в порядке?{/cps}"
    
    menu:
        "Девушка кажется подозрительной, стоит ли ей доверять?" 
        "Довериться":
            show defgg:
                xalign 0.9
                yalign -0.1
            
            a "{cps=25}Со мной всё в порядке{/cps}"
            e "{cps=25}Всегда рада помочь{/cps}"
            e "{cps=25}Ты помнишь, что с тобой произошло?{/cps}"
            a "{cps=25}К сожалению, я ничего не помню...{/cps}"
            e "{cps=25}Тогда собирайся, пойдём освежать твою память{/cps}"
            a "{cps=25}А куда мы пойдём?{/cps}"
            e "{cps=25}Тут неподалёку есть очень красивый сад{/cps}"
            a "{cps=25}В саду всегда так хорошо, пойдём скорее{/cps}"
            jump sad
            
            
        "Усомниться":
            a "{cps=25}Зачем ты меня привезла сюда? Я не знаю тебя.\nМожешь оставить меня одного?"
            show vg_1:
                xalign 0.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            with dissolve
            e "{cps=25}Ладно, я зайду позже." 
            show vg_1:
                xalign 10.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            show vg:
                xalign 10.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            with dissolve
            b "{cps=25}Я задавался вопросами:\nКто она такая и почему вообще привела меня к себе?{/cps}" 
            b "{cps=25}Я совершенно незнакомый человек для нее, и эти мысли навевали подозрения.{/cps}"
            b "{cps=25}Кто знает, какие у нее могут быть скрытые мотивы и что она прячет в своей голове.{/cps}"
            b "{cps=25}Резко в моих глазах потемнело...{/cps}"
            jump rejection
    return


label sad:
    scene forest1 with fade
    "Пока мы шли по тропинке - сад казался загадочным и прекрасным.В его густой зелени скрыты тысячи тайн и загадок" with dissolve
    "Резко я задумался о том, как давно эти деревья уже растут здесь, как много сменилось сезонов и как много видели они дождей и ветров."
    "Cквозь своим размышления, я услышал, что моя спасительница что-то начала говорить"
    
    scene forest2
    show defgg:
        xalign 0.9
        yalign -0.1
        
    show vg_1:
        xalign 0.2
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    with dissolve
    e "{cps=25}Cлушай, твои родители наверное переживают...{/cps}" 
    a "{cps=25}Не знаю, ведь я даже не могу вспомнить их лица{/cps}"
    e "{cps=25}В любом случае не переживай, по новостям бы уже передавали информацию о твоей пропаже{/cps}"
    a "{cps=25}Пойдём дальше{/cps}"
    
    scene bgfl2 with dissolve
    "Резко на глаза мне бросился красивый цветок"
    "Мне пришла мысль, а что если..."
    menu:
        "Подарить Эйлин в знак благодарности":
            scene forest2 with dissolve
            show flower:
                xzoom 0.5
                yzoom 0.5
            "Поздравляю, вы подарили цветок Эйлин.\nВозможно это повлияет на ваши отношения" with dissolve
            window hide
            $ renpy.pause()
            scene forest2
            show defgg:
                xalign 0.9
                yalign -0.1
                
            show vg_1:
                xalign 0.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            a "{cps=25}Спасибо тебе за спасение и за то, что помогаешь мне{/cps}" with dissolve
            show vg:
                xalign 0.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            e "{cps=25}Какой красивый!{/cps}"
            e "{cps=25}Спа...{/cps}"

        "Не стоит, зачем портить природу":
            "Действительно, зачем?"
            scene forest2
            show vg_1:
                xalign 0.2
                yalign -0.5
                xzoom 0.7
                yzoom 0.7
            show agrgg:
                xalign 0.9
                yalign -0.1
            


    show vg_1:
        xalign 0.2
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    show vg:
        xalign 10.2
        yalign -10.5
        xzoom 0.7
        yzoom 0.7
    show agrgg:
        xalign 0.9
        yalign -0.1
    with dissolve
    v "{cps=25}Неожиданно [input_name] схватился за дерево и его лицо помрачнело{/cps}" with dissolve
    
    
    
    e "{cps=25}Что с тобой?{/cps}"
    a "{cps=25}Голова болит и всё размытое...{/cps}"
    e "{cps=25}[input_name]!{/cps}"
    play sound "приступ.mp3" volume 0.03 if_changed
    scene hospital with fade
    b "{cps=25}Где я? Что со мной происходит?!{/cps}" with dissolve
    b "{cps=25}Почему я не могу двигаться?{/cps}"
    b "{cps=25}Это было очень похоже на сон, причём будто осознанный{/cps}"
    e "{cps=25}Очнись, прошу тебя{/cps}"
    play sound "рсэ.mp3" volume 0.03 if_changed
    scene forest2 with fade
    show surgg:
        xalign 0.9
        yalign -0.1
        
    show vg_1:
        xalign 0.2
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    
    e "{cps=25}[input_name], наконец-то ты пришёл в себя{/cps}" with dissolve
    e "{cps=25}Думаю на сегодня хватит прогулок, пойдём, заодно по пути расскажешь, что произошло{/cps} "
    scene scbefo with fade
    
    "Пока мы шли домой, довольно сильно стемнело" with dissolve
    show defgg:
        xalign 0.9
        yalign -0.1
        
    show vg:
        xalign 0.2
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    e "{cps=25}Так что же с тобой случилось?{/cps}" with dissolve
    a "{cps=25}Я видел какую-то комнату{/cps}"
    e "{cps=25}И что было в этой комнате?{/cps}"
    a "{cps=25}Я не мог пошевелиться и видел только один потолок{/cps}"
    a "{cps=25}Как будто бы я переместился из одной реальности в другую{/cps}"
    e "{cps=25}Думаю, ты не очень себя чувствуешь{/cps}"
    a "{cps=25}Наверное...{/cps}"
    show defgg:
        xalign 10.0
        yalign -0.1
    show vg_v2:
        xalign 0.09
        yalign -0.5
        xzoom 0.7
        yzoom 0.7

    show vg:
        xalign 10.0
    show surgg:
        xalign 0.25
        yalign -0.1
    "Вдруг раздался хруст веток и шелест листьев" with dissolve
    "Внезапно из-за кустов выходит старуха "
    
    show babka:
        xalign 0.9
        yalign -7.0
    gm "{cps=25}Молодой человек, извините за то, что подслушала вашу беседу, но я не могла не присоединиться{/cps}" with dissolve
    gm "{cps=25}Я вижу у вас непростое прошлое, которое вы не против узнать получше{/cps}"
    gm "{cps=25}Ах, вам уже удалось немного побывать там{/cps}"
    a "{cps=25}Да, я пытался вспомнить своё прошлое, но что-то не сходится, всё в голове как-будто бы перепуталось{/cps}"
    gm "{cps=25}Понимаю, воспоминания могут быть сложными и непредсказуемыми, но я чувствую, что вы в опасности{/cps}"
    a "{cps=25}В каком смысле в опасности?{/cps}"
    gm "{cps=25}Это я смогу вам сказать, когда вы определитесь с выбором.{/cps}"
    e "{cps=25}С каким это ещё выбором?{/cps}"
    gm "{cps=25}Ему предстоит выбрать: остаться здесь и сейчас или же я могу помочь вспомнить прошлое, но я не могу сказать точно, что будет если ты всё вспомнишь{/cps}"
    gm "{cps=25}Так что?{/cps}"
    
    menu:
        "Выберите дальнейшее действие"
        "Остаться здесь и сейчас":
            scene grass with fade
            "Я посмотрел под ноги, где шелестела трава и задумался..." with dissolve
            "Я вспоминал Эйлин..."
            scene fb with dissolve
            "Какая она всё таки красивая" with dissolve
            scene fb2 with dissolve
            "Я будто бы нашёл своего человека" with dissolve
            jump baddec
        "Вспомнить прошлое":
            scene grass with fade
            "Я посмотрел под ноги, где шелестела трава и задумался..." with dissolve
            "Я подумал о Эйлин"
            scene fb with dissolve
            "Она хороший человек..." with dissolve
            scene fb2 with dissolve
            "За то время, пока я с ней общался, я привязался к ней" with dissolve
            "Я не понимаю, что будет правильнее"
            "Я запутался..."
            menu:
                "Ещё не поздно всё изменить"
                "Передумать":
                    jump baddec
                "Оставить свой выбор":
                    scene grass with fade
                    a "{cps=25}Думаю, я должен узнать всю правду{/cps}" with dissolve
                    a "{cps=25}Я не смогу жить не зная откуда и почему я здесь{/cps}"
                    a "{cps=25}Всё это время, пока я видел видения, я чувствовал, что я на своём месте{/cps}"
                    a "{cps=25}Думаю узнать правду - это правильное решение{/cps}"
                    
                    scene scbefo with fade 
            
                    show defgg:
                        xalign 0.25
                        yalign -0.1
                    show vg:
                        xalign 0.09
                        yalign -0.5
                        xzoom 0.7
                        yzoom 0.7
                    show babka:
                        xalign 0.9
                        yalign -7.0 
                    a "{cps=25}Я всё таки хочу узнать всю правду{/cps}" with dissolve
                    a "{cps=25}Что мне нужно сделать?{/cps}"
                    gm "{cps=25}Тут неподалёку моя хижина, всё нужное в ней.{/cps}"
                    scene izba with fade
                    show vg_1:
                        xalign 0.05
                        yalign -1.5
                        xzoom 0.6
                        yzoom 0.6
                    show defgg:
                        xalign 0.15
                        yalign -0.4
                        xzoom 0.85
                        yzoom 0.85
                    show babka:
                        xalign 0.9
                        yalign 1.6
                        xzoom 0.85
                        yzoom 0.85
                    gm "{cps=25}Вот и она. Проходите внутрь аккуратно, не ударьтесь головой{/cps}" with dissolve
                    b "{cps=25}Хижина выглядит довольно старой и ветхой{/cps}"
                    a "{cps=25}Нам точно стоит туда заходить? Она не выглядит безопасной{/cps}"
                    gm "{cps=25}Так, кто из нас хочет вспомнить своё прошлое?{/cps}"
                    a "{cps=25}Ладно, ладно{/cps}"
                    play sound "дуб.mp3" volume 0.03 if_changed
                    scene izba1 with fade
                    show defgg:
                        xalign 0.25
                        yalign -0.1
                    show vg_1:
                        xalign 0.09
                        yalign -0.5
                        xzoom 0.7
                        yzoom 0.7
                    show babka:
                        xalign 0.9
                        yalign -7.0 
                    with dissolve
                    gm "{cps=25}Добро пожаловать в мой дом, надеюсь здесь ты найдёшь ответы, которые ищешь{/cps}" 
                    gm "{cps=25}Мне нужно поискать книгу с рецептом, подождите меня тут{/cps}"
                    show babka:
                        xalign 10.9
                        yalign -7.0 
                    b "{cps=25}Я решил осмотреть хижину, чтобы понять, кого из себя представляет эта старуха{/cps}"
                    window hide
                    call screen izba
                    with dissolve

                    label izba_prod:
                        "Послышались шаги из комнаты в которую ушла старуха"
                        
                        scene izba1
                        show babka:
                            xalign 0.9
                            yalign -7.0
                        show defgg:
                            xalign 0.25
                            yalign -0.1
                        show vg_1:
                            xalign 0.09
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7 
                        gm "{cps=25}Я нашла книгу, но мне нужно время, чтобы приготовить зелье{/cps}" with dissolve
                        show babka:
                            xalign 0.9
                            yalign -7.0
                        gm "{cps=25}Можете прогуляться пока что вокруг хижины, я позову, когда закончу{/cps}"
                        play sound "osnova.mp3" volume 0.07 if_changed
                        scene izba with fade
                        show defgg:
                            xalign 1.0
                            yalign -0.1
                        show vg4:
                            xalign 0.15
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7 
                        with dissolve
                        e "{cps=25}Мне не по себе в этом месте. Меня беспокоит, что старуха использует темные чары. Может быть, нам стоит быть осторожными{/cps}" with dissolve
                        a "{cps=25}Может быть ты права, но с другой стороны у меня нет другого выбора, мне нужно попробовать все возможности{/cps}"
                        e "{cps=25}Ох, хорошо, я полагаюсь на твой выбор, но мне всё равно страшно{/cps}"
                        show vg_1:
                            xalign 0.15
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7
                        show vg4:
                            xalign 10.15
                        with dissolve
                        "{cps=25}[input_name] увидев то, как Эйлин начала вытирать свои глаза, подошёл к ней и крепко обнял её{/cps}" with dissolve
                        a "{cps=25}Не волнуйся, я думаю всё пройдёт хорошо.{/cps}"
                        show vg_1:
                            xalign 10.15
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7
                        show vg4:
                            xalign 0.15
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7
                        with dissolve
                        e "{cps=25}Ты точно хочешь вспомнить своё прошлое?{/cps}" with dissolve          
                        a "{cps=25}Да, я в этом уверен{/cps}"
                        "Вдруг послышался голос старухи из окна"
                        gm "{cps=25}Зелье готово{/cps}"
                        play sound "дуб.mp3" volume 0.03 if_changed
                        scene izba1 with fade
                        show defgg:
                            xalign 0.25
                            yalign -0.1
                        show vg_1:
                            xalign 0.09
                            yalign -0.5
                            xzoom 0.7
                            yzoom 0.7
                        show babka:
                            xalign 0.9
                            yalign -7.0 
                        "Cтаруха протянула мне зелье" with dissolve
                        gm "{cps=25}Пей до дна{/cps}"
                        b "{cps=25}Я взял зелье и сделал один глоток, моё тело сразу же начала обволакивать странная лёгкость{/cps}"
                        b "{cps=25}Постепенно мои глаза закрывались, мне стало немного страшно{/cps}"
                        b "{cps=25}Но дороги назад уже нет{/cps}"
                        b "{cps=25}Но вот уже последняя капля спускалась по моей гортани{/cps}"
                        b "{cps=25}Я как будто бы перестал чувствовать своё тело{/cps}"
                        scene black with fade
                        "{cps=15}Темнота окружает меня, словно плотный туман и я не могу разобрать ничего{/cps}"
                        "{cps=15}Я не уверен, где я нахожусь и чувствую себя, как будто я плаваю в бесконечном море{/cps}"
                        "{cps=15}А что если я умер?{/cps}"
                        "{cps=15}Что если это всё сон?{/cps}"
                        "{cps=15}Или может быть я на грани между жизнью и смертью?{/cps}"
                        "{cps=15}Вдалеке я увидел некий свет, который приближался ко мне{/cps}"
                        jump godend
    return


screen izba:
    imagemap:
        hover 'images/bgivn_hover.jpg'
        idle 'images/bgivn_idle.jpg'
        hotspot ((654, 232, 249, 296)) action Jump("obj1")
        # картина
        hotspot ((72, 673, 172, 153)) action Jump("obj2") 
        # череп
        hotspot ((1342, 431, 285, 227)) action Jump("obj3")
        # статуэтка
        hotspot ((540, 790, 198, 165)) action Jump("obj4")
        # книга

label obj1:
    $ next_stage_v1 += 1
    if next_stage_v1 == 4:
        scene bgivn_idle
        "Какая странная картина, интересно, что же она обозначает?"

        b "{cps=25}По всей видимости старуха занимается тёмной магией{/cps}"  
        b "{cps=25}Думаю, больше ничего интересного здесь я не найду{/cps}"
        jump izba_prod
    else:
        scene bgivn_idle
        "Какая странная картина, интересно, что же она обозначает?"
        call screen izba

label obj2:
    $ next_stage_v1 += 1
    if next_stage_v1 == 4:
        scene bgivn_idle
        "Что тут делает череп? Неужели настоящий?"
        "Надеюсь, что он искуственный"
        b "{cps=25}По всей видимости старуха занимается тёмной магией{/cps}"  
        b "{cps=25}Думаю, больше ничего интересного здесь я не найду{/cps}"
        jump izba_prod
    else:
        scene bgivn_idle
        "Что тут делает череп? Неужели настоящий?"
        "Надеюсь, что он искуственный"
        call screen izba

label obj3:
    $ next_stage_v1 += 1
    if next_stage_v1 == 4:
        scene bgivn_idle
        "Кажется, это статуэтка ангела"
        "Она такая же жуткая, как и остальные предметы в комнате"
        b "{cps=25}По всей видимости старуха занимается тёмной магией{/cps}"  
        b "{cps=25}Думаю, больше ничего интересного здесь я не найду{/cps}"
        jump izba_prod
    else:
        scene bgivn_idle
        "Кажется, это статуэтка ангела"
        "Она такая же жуткая, как и остальные предметы в комнате"
        call screen izba

label obj4:
    $ next_stage_v1 += 1
    if next_stage_v1 == 4:
        scene bgivn_idle
        'Кажется это книга'
        "'Книга теней и света'"
        'Что заставило её оставить такую реликвию на полу?'
        'Небрежность или скрытый умысел?'
        b "{cps=25}По всей видимости старуха занимается тёмной магией{/cps}"  
        b "{cps=25}Думаю, больше ничего интересного здесь я не найду{/cps}"
        jump izba_prod
    else:
        scene bgivn_idle
        'Кажется это книга'
        "'Книга теней и света'"
        'Что заставило её оставить такую реликвию на полу?'
        'Небрежность или скрытый умысел?'
        call screen izba

label baddec:
    scene grass with fade
    "Думаю в прошлом я был не очень хорошим человеком" with dissolve
    "К тому же старуха говорила о какой-то опасности"
    "Думаю она мне сейчас ни к чему."
    "С Эйлин мне хорошо..."
    "Думаю я сделал правильный выбор"
    scene scbefo
    show defgg:
        xalign 0.25
        yalign -0.1
    show vg4:
        xalign 0.09
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    show babka:
        xalign 0.9
        yalign -7.0
    with fade
    
    e "{cps=25}И что же ты выбрал, [input_name]?{/cps}" with dissolve
    show vg:
        xalign 0.09
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    show vg4:
        xalign 10.09
        yalign -0.5
        xzoom 0.7
        yzoom 0.7
    a "{cps=25}Эйлин, я надеюсь ты не против, если я останусь с тобой{/cps}"
    e "{cps=25}Конечно не против!{/cps}"
    a "{cps=25}Спасибо за помощь, но я выбрал свой путь.{/cps}"
    a "{cps=25}Я не хочу знать своё прошлое{/cps}"
    gm "{cps=25}Что ж, как знаешь{/cps}"
    show babka:
        xalign 10.0
    with dissolve
    window hide
    $ renpy.pause()
    scene e1 with dissolve
    "[input_name] остался с Эйлин" with dissolve
    scene e2 with dissolve
    "У них было всё хорошо, с каждым днём они сближались всё больше и больше" with dissolve
    scene e3 with dissolve
    "А главное, что им было хорошо вместе..." with dissolve
    "Никакие трудости не казались им страшными, ведь они знали, что вмести они смогут преодолеть всё"
    scene black with fade
    "{cps=15}А на самом деле...{/cps}" with dissolve
    "{cps=15}Это был всего лишь сон...{/cps}"
    "{cps=12}Из которого он не смог выбраться...{/cps}"
    
    return

label rejection:
    play sound "приступ.mp3" volume 0.07 if_changed
    scene hospital_blur with fade
    b "{cps=25}Где я? Что со мной происходит?!{/cps}" with dissolve
    b "{cps=25}Почему я не могу двигаться?{/cps}" 
    b "{cps=25}Это было очень похоже на сон, причём будто осознанный{/cps}" 
    "Думаю стоит попытаться что-то предпринять"
    
    menu:
        "Очнуться":
            $ click =+ 1            
        "Очнуться":
            $ click =+ 1
        "Очнуться":
            $ click =+ 1
    if click == 1:
        menu: 
            "Почему мне так трудно прийти в сознание?" 
            "Очнуться":
                $ click =+ 2
            "Очнуться":
                $ click =+ 2
    if click == 2:
        menu:
            "Что мешает мне очнуться??"
            "Очнуться":
                $ click =+ 3
    
    b "{cps=25}А что если мне не стоит спешить с пробуждением?{/cps}"
    b "{cps=25}Возможно, в моем бессознательном состоянии я нахожусь в безопасности.{/cps}"
    b "{cps=25}Я чувствую, что мое присутствие здесь имеет какое-то значение.{/cps}"

    if click == 3:
        menu:
            "Примите собственное решение."
            "Попытаться пробудиться":
                jump asd
            "Остаться":
                play sound "ксм.mp3" volume 0.07 if_changed
                "Неожиданно я услышал голос"
                "Женский голос"
                scene med with fade
                w "{cps=25}Очнулся.{/cps}" with dissolve
                scene hospital_blur with fade
                b "{cps=25}Медсестра сказала, что я пролежал без сознания где то 3 месяца.{/cps}" with dissolve

                b "{cps=25}А все что я видел раньше?{/cps}"
                b "{cps=25}Что же это было?{/cps}"
                b "{cps=25}Простой сон?{/cps}"
                b "{cps=25}Иллюзия?{/cps}"

    return
    
label godend:
    scene hospital_blur with fade
    play sound "ксм.mp3" volume 0.07 if_changed
    "Я вновь увидел тот самый потолок" with dissolve
    "Неожиданно я услышал голос"
    "Женский голос"
    scene med with fade
    w "{cps=20}Очнулся.{/cps}" with dissolve
    scene hospital_blur with fade
    b "{cps=25}Медсестра сказала, что я пролежал без сознания где то 3 месяца.{/cps}" with dissolve
    b "{cps=25}А все что я видел раньше?{/cps}"
    b "{cps=25}Что же это было?{/cps}"
    b "{cps=25}Простой сон?{/cps}"
    b "{cps=25}Иллюзия?{/cps}"
    return



label asd:
    play sound "рсэ.mp3" volume 0.03 if_changed
    scene bg with fade
    show agrgg:
        xalign 0.9
        yalign -0.1
    with dissolve
    a "{cps=25}Что это было?!{/cps}"
    a "{cps=25}Это было настолько реалистично, что я теперь не знаю, где настоящая реальность{/cps}"
    a "{cps=25}Думаю стоит пойти прогуляться{/cps}"
    scene sh with fade
    a "{cps=25}Когда я выходил из дома Эйлин я там не увидел...{/cps}" with dissolve
    a "{cps=25}Надеюсь, я её не обидел{/cps}"
    a "{cps=25}Я понимаю её{/cps}"
    a "{cps=25}На её месте я бы выгнал себя{/cps}"
    a "{cps=25}Я чувствую себя ужасно, думаю по приходу обратно стоит извиниться {/cps}"
    scene park_idle
    "Я и не заметил, как я дошёл до парка, пока думал об этом"
    "Парк выглядит довольно интересным, думаю стоит осмотреться"
    window hide
    call screen park 
    with dissolve

screen park:
    imagemap:
        hover 'images/park_hover.jpg'
        idle 'images/park_idle.jpg'
        hotspot ((379, 532, 327, 208)) action Jump("kust")
        hotspot ((933, 790, 217, 114)) action Jump("banan")
        hotspot ((933, 547, 98, 103)) action Jump("ball")
        hotspot ((1337, 586, 219, 101)) action Jump("golub")

screen parkv2:
    imagemap:
        hover 'images/park_hover_v2.jpg'
        idle 'images/park_idle_v2.jpg'
        hotspot ((379, 532, 327, 208)) action Jump("kust")
        hotspot ((933, 790, 217, 114)) action Jump("banan")
        hotspot ((933, 547, 98, 103)) action Jump("ball")
        hotspot ((1337, 586, 219, 101)) action Jump("golub")

label kust:
    $ next_stage += 1
    if next_stage == 4:
        scene park_idle_v2
        'Куст, как куст. Зелёный, шелестит на ветру'
        'Не знаю, что от него ожидать. Может он что-то помнит? Или прячет в своей листве обрывок чьей-то забытой истории?'
        'В моей голове пусто. Не единой зацепки, ни намёка на то, кто же я такой'
        "Больше мне здесь делать нечего."
        jump park_prod
    elif banan == False:
        scene park_idle
        'Куст, как куст. Зелёный, шелестит на ветру'
        'Не знаю, что от него ожидать. Может он что-то помнит? Или прячет в своей листве обрывок чьей-то забытой истории?'
        'В моей голове пусто. Не единой зацепки, ни намёка на то, кто же я такой'
        call screen park
    else:
        scene park_idle_v2
        'Куст, как куст. Зелёный, шелестит на ветру'
        'Не знаю, что от него ожидать. Может он что-то помнит? Или прячет в своей листве обрывок чьей-то забытой истории?'
        'В моей голове пусто. Не единой зацепки, ни намёка на то, кто же я такой'
        call screen parkv2


label banan:
    $ next_stage += 1
    if next_stage == 4:
        scene park_idle
        'Желтая кожура банана на фоне ухоженной зелени парка резанула по глазам'
        'Неужели так сложно донести мусор до урны?!'
        'Неприятно осозновать, что есть люди, которым чужды даже элементарные правила приличия'
        'Пожалуй, стоит убрать этот мусор'
        menu:
            'Убрать':
                $ banan = True
                scene park_idle_v2
                'Так-то лучше'
        "Больше мне здесь делать нечего."
        jump park_prod
    else:
        scene park_idle
        'Желтая кожура банана на фоне ухоженной зелени парка резанула по глазам'
        'Неужели так сложно донести мусор до урны?!'
        'Неприятно осозновать, что есть люди, которым чужды даже элементарные правила приличия'
        'Пожалуй, стоит убрать этот мусор'
        menu:
            'Убрать':
                $ banan = True
                call screen parkv2
                with dissolve

label golub:
    $ next_stage += 1
    if next_stage == 4:
        scene park_idle_v2
        'Голубь невозмутимо сидел на тропинке, словно каменная статуя среди живой зелени парка.'
        'Странно, почему он не улетает?'
        'Неужели он не боится меня? Совершенно непугливый'
        'Может с ним что-то случилось?'
        "Больше мне здесь делать нечего."
        jump park_prod
    elif banan == False:
        scene park_idle
        'Голубь невозмутимо сидел на тропинке, словно каменная статуя среди живой зелени парка.'
        'Странно, почему он не улетает?'
        'Неужели он не боится меня? Совершенно непугливый'
        'Может с ним что-то случилось?'
        call screen park
    else:
        scene park_idle_v2
        'Голубь невозмутимо сидел на тропинке, словно каменная статуя среди живой зелени парка.'
        'Странно, почему он не улетает?'
        'Неужели он не боится меня? Совершенно непугливый'
        'Может с ним что-то случилось?'
        call screen parkv2

label ball:
    $ next_stage += 1
    if next_stage == 4:
        scene park_idle_v2
        'Обычный мяч, немного выцветший.'
        'Наверное, кто-то из детей оставил'
        "Больше мне здесь делать нечего."
        jump park_prod
    elif banan == False:
        scene park_idle_v2
        'Обычный мяч, немного выцветший.'
        'Наверное, кто-то из детей оставил'
        call screen park
    else:
        scene park_idle_v2
        'Обычный мяч, немного выцветший.'
        'Наверное, кто-то из детей оставил'
        call screen parkv2


label park_prod:
    scene park_idle_v2  
    "Думаю, стоит пройтись дальше" 
    scene park_next_stage
    with fade
    "Я прошёл вглубь парка" with dissolve
    play sound "приступ.mp3" volume 0.03 if_changed
    "Резко мне стало плохо" 
    scene sky
    with fade
    "Я упал на землю" with dissolve
    "Вскоре мои глаза начали закрываться"
    
    scene black
    with fade

    "{cps=20}Может я уснул?{/cps}" with dissolve
    "{cps=20}Или cнова отключился?{/cps}" with dissolve
    "{cps=20}Странно, но я не вижу каких то видений, и это не похоже на мой утренний приступ..{/cps}" with dissolve
    "Внезапно послышался незнакомый голос из этой пустоты" with dissolve
    "-Молодой человек" with dissolve
    scene sky
    with fade
    "Я вновь очнулся" with dissolve
    play sound "рсэ.mp3" volume 0.03 if_changed
    scene park_next_stage with dissolve
    show babka:
        xalign 0.85
        yalign -7.0

    show surgg:
        xalign 0.1
        xzoom 0.9
        yzoom 0.9
        yalign -0.2

    "Передо мной стояла какая-то женщина" with dissolve
    gm "{cps=25}С вами всё хорошо?{/cps}"
    a "{cps=25}Да, не переживайте, у меня это не первый раз за сегодня{/cps}"
    gm "{cps=25}Это очень плохо{/cps}"
    gm "{cps=25}Что ж, я могу вам помочь{/cps}"
    a "{cps=25}Как вы можете мне помочь?{/cps}"
    gm "{cps=25}Я чуствую, что вы в опасности и ваши сновидения возникают не просто так{/cps}"
    gm "{cps=25}К тому же я вижу, что вы не помните половину своей жизни и не прочь узнать о ней по больше{/cps}"
    a "{cps=25}Да, я пытался вспомнить, но что-то не получается{/cps}"
    gm "{cps=25}Тебе предстоит выбрать: остаться с девушкой, которая тебе помогла или же я могу тебе помочь вспомнить прошлое{/cps}"
    a "{cps=25}Откуда вы знаете Эйлин, вы знакомы с ней?{/cps}"
    gm "{cps=25}Я многое знаю, я ведь гадалка{/cps}"
    gm "{cps=25}На самом деле девушка - очень хороший человек{/cps}"
    gm "{cps=25}Она помогла тебе не из какого-то плохого побуждения{/cps}"
    gm "{cps=25}Так что выбор за тобой{/cps}"
    gm "{cps=25}Если решишь вспомнить прошлое - приходи ко мне. Я помогу тебе{/cps}"
    "Старуха протянула мне лист, где написано, как к ней добраться"
    show babka:
        xalign 10.0
    show surgg:
        xalign 0.5
        xzoom 0.9
        yzoom 0.9
        yalign -0.2
    "И ушла" with dissolve
    show agrgg:
        xalign 0.5
        xzoom 0.9
        yzoom 0.9
        yalign -0.2
    show surgg:
        xalign 10.0
    "Я начал обдумывать то, что сказала гадалка" with dissolve
    "Она может помочь мне вспомнить прошлое"
    "Я смогу найти своих родных"
    "Мои приступы закончатся и исчезнет чуство неопределённости"
    show agrgg:
        xalign 10.0
    show surgg:
        xalign 0.5
        xzoom 0.9
        yzoom 0.9
        yalign -0.2
    with dissolve
    
    "Пока я думал об этом, вдалеке появился знакомый силуэт" with dissolve
    show vg4:
        yalign -0.4
        xalign 0.15
        xzoom 0.7
        yzoom 0.7
    show agrgg:
        xalign 10.7
        xzoom 0.9
        yzoom 0.9
        yalign -0.2
    show surgg:
        xalign 0.9
        yalign -0.2
        xzoom 0.9
        yzoom 0.9
    with fade
    a "{cps=25}Что ты тут делаешь?{/cps}" with dissolve
    e "{cps=25}Тебя долго не было дома - я волновалась{/cps}" 
    e "{cps=25}С тобой всё хорошо?{/cps}"
    a "{cps=25}Да, со мной всё в порядке, я скоро вернусь{/cps}"
    a "{cps=25}Мне надо побыть одному{/cps}"
    e "{cps=25}Хорошо, буду ждать{/cps}"
    show vg4:
        xalign 10.0
    show defgg:
        xalign 0.5
        yalign -0.2
        xzoom 0.9
        yzoom 0.9
    show surgg:
        xalign 10.0
    with dissolve
    "Я подумал о Эйлин"
    "Старуха сказала, что она хороший человек"
    "Может в своём прошлом я был плохим человеком"
    "А Эйлин мне досталась, как подарок судьбы"
    "Тяжело..."
    menu:
        'Выберите дальнейшее действие'
        "Вспомнить прошлое":
            jump godendv2
        "Остаться с Эйлин":
            jump badendv2

label godendv2:
    a "{cps=25}Что ж, пока совсем не стемнело, стоит поторопиться.{/cps}"
    scene forest1 with dissolve
    "Я поспешил на поиски того самого адреса, где живёт старуха"
    "В моей голове были только одни мысли: вспомнить."
    "В голове пустота и зияющая дыра вместо прошлого"
    "Да, воспоминания могут быть болезнеными, но разве невидение - не наказание?"
    "Я прошёл дальше"
    scene forest2 with dissolve
    "Это странная девушка..." with dissolve
    "Она спасла меня, это верно. Но интуиция шепчет - ей нельзя доверять."
    "Где-то глубоко под пеленой амнезии теплится уверенность: меня ждут."
    "Близкие."
    "Родные."
    "И ради них стоит рискнуть"
    scene izba with dissolve
    a "{cps=25}Кажется это здесь{/cps}" with dissolve
    scene izba:
        xzoom 1.4
        yzoom 1.4
        xalign 0.5
        yalign 0.75
    "Я стремительно пустился к двери старухи" with dissolve
    "Как ни странно, но как только я подошёл к двери - её открыла старуха"
    play sound "дуб.mp3" volume 0.03 if_changed
    scene izba1 with dissolve
    
    show defgg:
        xalign 0.1
        yalign -0.1
    show babka:
        xalign 0.85
        yalign -7.0 
    gm "{cps=25}Рада снова тебя видеть, [input_name]{/cps}" with dissolve
    a "{cps=25}Здравствуйте, я пришёл, чтобы вы помогли мне вспомнить прошлое{/cps}"
    gm "{cps=25}Да, конечно, я как раз нашла книгу рецептов{/cps}"
    gm "{cps=25}Только есть одно но. У меня нет некоторых ингридиентов, не мог бы ты их поискать?{/cps}"
    a "{cps=25}Без проблем{/cps}"
    "Старуха подала мне листок, на котором написано - каких ингридиентов не хватает"
    "Трава, шишки, бамбук, перо - странный набор"
    "Я принялся за работу"
    $ InitGame("izba", 15.0, (1565, 670), "cone.png", (400, 683), "grassivn", (805, 850), "stylus", (1300, 690), "bambuk")
    $ GameAsBG()
    
    with dissolve

    "Шишки, бамбук... И где же это я найду?"

    $ res = StartGame()
    $ GameAsBG()
    scene izba with fade
    "Что ж, я думал это будет сложнее" with dissolve
    "Нужно возвращаться к старухе"
    scene izba1 with fade
    show defgg:
        xalign 0.1
        yalign -0.1
    show babka:
        xalign 0.85
        yalign -7.0  
    a "{cps=25}Я принёс всё что нужно{/cps}" with dissolve
    gm "{cps=25}Это хорошо.{/cps}"
    'Старуха взяла все ингредиенты и вложила их в пузырёк с зельем'
    'А затем протянула его мне'
    gm "{cps=25}Пей до дна{/cps}"
    b "{cps=25}Я взял зелье и сделал один глоток, моё тело сразу же начала обволакивать странная лёгкость{/cps}"
    show agrgg:
        xalign 0.1
        yalign -0.1
    show defgg:
        xalign 10.0
    with dissolve
    b "{cps=25}Постепенно мои глаза закрывались, мне стало немного страшно{/cps}" with dissolve
    b "{cps=25}Но дороги назад уже нет{/cps}"
    b "{cps=25}Но вот уже последняя капля спускалась по моей гортани{/cps}"
    b "{cps=25}Я как будто бы перестал чувствовать своё тело{/cps}"
    scene black with fade
    "{cps=12}Темнота окружает меня, словно плотный туман и я не могу разобрать ничего{/cps}" with dissolve
    "{cps=20}Я не уверен, где я нахожусь и чувствую себя, как будто я плаваю в бесконечном море{/cps}"
    "{cps=12}А что если я умер?{/cps}"
    "{cps=12}Что если это всё сон?{/cps}"
    "{cps=10}Или может быть я на грани между жизнью и смертью?{/cps}"
    "{cps=20}Вдалеке я увидел некий свет, который приближался ко мне{/cps}"
    jump godend
    return

label badendv2:
    scene park_next_stage
    show defgg:
        yalign -0.2
        xzoom 0.9
        yzoom 0.9
        xalign 0.5
    "Я принял решение - остаюсь с Эйлин, кто знает каким окажется моё прошлое"
    "И к тому же не хочется доверять какой-то первовстречной старухе"
    "Пока я обдумывал своё решение - уже довольно стемнело"
    "Думаю пора домой"
    scene sh with fade
    "Я стремительно шёл домой, чтобы рассказать Эйлин о событиях, которые произошли со мной в парке" with dissolve
    
    scene home
    with fade
    "И вот наконец-то я зашёл в дом" with dissolve
    "Мою душу охватило приятное ощущение"
    a "{cps=25}Эйлин, я дома!{/cps}"
    scene h1 with dissolve
    "[input_name] остался с Эйлин" with dissolve
    scene h2 with dissolve
    "У них было всё хорошо, с каждым днём они сближались всё больше и больше" with dissolve
    scene h3 with dissolve
    "А главное, что им было хорошо вместе..." with dissolve
    "Никакие трудости не казались им страшными, ведь они знали, что вмести они смогут преодолеть всё"
    scene black with fade
    "{cps=20}А на самом деле...{/cps}"
    "{cps=15}Это был всего лишь сон...{/cps}"
    "{cps=12}Из которого он не смог выбраться...{/cps}"

