def on_button_pressed_a():
    global Suma_1
    if Suma_1 == 0:
        Suma_1 = 1
    elif Suma_1 == 1:
        Suma_1 = 2
    elif Suma_1 == 3:
        music.play_melody("G C C D D E F G ", 500)
        Suma_1 = 4
        basic.show_string("Conejo Elena")
    else:
        Suma_1 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if Suma_1 == 3:
        basic.show_icon(IconNames.EIGTH_NOTE)
        music.begin_melody(["g4:2",
                "c5",
                "c",
                "d",
                "d",
                "e:4",
                "f:2",
                "g",
                "f",
                "e",
                "e",
                "d",
                "d",
                "c",
                "g",
                "f",
                "e",
                "e",
                "e",
                "f",
                "e",
                "d",
                "d",
                "g",
                "f",
                "e",
                "e",
                "e",
                "f",
                "e",
                "d",
                "d",
                "d",
                "g",
                "e",
                "c",
                "d",
                "d",
                "c"],
            MelodyOptions.ONCE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Suma_1
    if Suma_1 == 2:
        Suma_1 = 3
    else:
        Suma_1 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

Suma_1 = 0
Suma_1 = 0
Melodia = "[f f]"

def on_forever():
    if Suma_1 == 0:
        basic.clear_screen()
basic.forever(on_forever)
