input.onButtonPressed(Button.A, function () {
    if (Suma_1 == 0) {
        Suma_1 = 1
    } else if (Suma_1 == 1) {
        Suma_1 = 2
    } else if (Suma_1 == 3) {
        music.playMelody("G C C G D E F G ", 411)
        Suma_1 = 4
        basic.showString("Conejo Elena")
    } else {
        Suma_1 = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    if (Suma_1 == 3) {
        basic.showIcon(IconNames.EigthNote)
        music.beginMelody(["g4:2", "c5", "c", "d", "d", "e:4", "f:2", "g", "f", "e", "e", "d", "d", "c", "g", "f", "e", "e", "e", "f", "e", "d", "d", "g", "f", "e", "e", "e", "f", "e", "d", "d", "d", "g", "e", "c", "d", "d", "c"], MelodyOptions.Once)
    }
})
input.onButtonPressed(Button.B, function () {
    if (Suma_1 == 2) {
        Suma_1 = 3
    } else {
        Suma_1 = 0
    }
})
let Suma_1 = 0
Suma_1 = 0
let Melodia = "[f f]"
basic.forever(function () {
    if (Suma_1 == 0) {
        basic.clearScreen()
    }
})
