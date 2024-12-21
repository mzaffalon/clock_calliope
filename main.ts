let y = 0
let x = 0
let helligkeit = 255
loops.everyInterval(100, function () {
    led.plotBrightness(x, y, helligkeit)
    if (x != 4) {
        x += 1
    } else {
        x = 0
        if (y != 4) {
            y += 1
        } else {
            y = 0
            if (helligkeit != 0) {
                helligkeit = 0
            } else {
                helligkeit = 255
            }
        }
    }
})
