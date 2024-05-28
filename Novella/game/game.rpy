init python:
    # окно по центру экрана
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # автоматическое объявление спрайтов
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ["images"]
    oXY = []
    oN = []
    oLen = 0
    maxLen = 0
    oBg = ""
    oLast = -1
    oTime = 0.0
    oMaxTime = 5.0
    needTimer = False
    oActive = False
    oRes = False

    # Инициализация игры, размещение предметов на экране
    def InitGame(bg, time, *args):
        global oBg, oXY, oN, oLen, maxLen, oLast, oTime, oMaxTime, oActive, needTimer, oRes
        oXY = []
        oN = []
        oLen = 0
        oBg = bg
        oLast = -1
        oTime = time
        oMaxTime = time
        maxLen = 0
        oActive = True
        oRes = False
        if oTime > 0.0:
            needTimer = True
        for xy, obj_name in zip(args[0::2], args[1::2]):
            oXY.append(xy)
            oN.append(obj_name)
            maxLen += 1

    # Запуск игры
    def StartGame():
        global oActive
        oActive = True
        need = True
        while need:
            renpy.call_screen("game", _layer="master")
            need = oRes == False
            if needTimer and (oTime <= .0):
                need = False

    # Показать экран игры в виде неактивного фона
    # Уже найденные предметы не будут отображаться
    def GameAsBG():
        global oActive
        oActive = False
        renpy.show_screen("game", _layer="master")

    # Обработчик клика по предмету
    def o_click(i):
        global oLen, oRes
        if i >= 0:
            if oN[i]:
                temp = oN[i]
                oN[i] = ""
                oLen += 1
                # renpy.play("sounds/click.mp3", channel="sound")
                renpy.restart_interaction()
                if needTimer:
                    if oLen >= maxLen:
                        oRes = True
                else:
                    oRes = temp
    oClick = renpy.curry(o_click)

# Собственно экран игры, запускать из функции StartGame()
screen game:
    modal True
    if oActive and needTimer:
        timer 0.01 repeat True action [SetVariable("oTime", oTime-.01), If(oTime <= .0, true=[Return()])]
    add oBg
    for i in range(0, len(oN)):
        if oN[i]:
            imagebutton:
                focus_mask True
                pos(oXY[i])
                idle oN[i]
                hover oN[i]
                # можно продублировать картинки предметов,
                # назвав их "images/имяпредмета_hover.png"
                # и высветить их в графическом редакторе
                # и заменить строку выше на строку ниже
                # тогда при наведении курсора, они будут подсвечиваться
                # hover oN[i] + " hover"
                if oActive:
                    action [oClick(i), Return()]
                else:
                    action []
    if oActive and needTimer:
        # if oTime > .1:
            # text "[oTime]" align(.1, .1) size 48
        # else:
            # text "0.0" align(.1, .1) size 48
        bar value StaticValue(oTime, oMaxTime):
            align(.5, .001)
            xmaximum 400
            ymaximum 20
            left_bar Frame("slider_left.png", 10, 10)
            right_bar Frame("slider_right.png", 10, 10)
            thumb None
            thumb_shadow None