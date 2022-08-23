input.onButtonPressed(Button.A, function () {
    if (Suma_1 == 0) {
        Suma_1 = 1
    } else if (Suma_1 == 1) {
        Suma_1 = 2
    } else if (Suma_1 == 3) {
        music.playMelody("C5 B A G F E D C ", 120)
        basic.showString("Abre la nevera")
    } else {
        Suma_1 = 0
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
basic.forever(function () {
    if (Suma_1 == 0) {
        basic.clearScreen()
    }
})
