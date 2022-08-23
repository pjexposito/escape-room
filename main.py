import music

def on_button_pressed_a():
    global Suma_1
    if Suma_1 == 0:
        Suma_1 = 1
    elif Suma_1 == 1:
        Suma_1 = 2
    elif Suma_1 == 3:
        music.play_melody("C5 B A G F E D C ", 120)
        basic.show_string("Abre la nevera")
    else:
        Suma_1 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Suma_1
    if Suma_1 == 2:
        Suma_1 = 3
    else:
        Suma_1 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Suma_1 = 0
Suma_1 = 0

def on_forever():
    if Suma_1 == 0:
        basic.clear_screen()
basic.forever(on_forever)
