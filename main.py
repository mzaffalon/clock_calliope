y = 0
x = 0
helligkeit = 255

def on_every_interval():
    global x, y, helligkeit
    led.plot_brightness(x, y, helligkeit)
    if x != 4:
        x += 1
    else:
        x = 0
        if y != 4:
            y += 1
        else:
            y = 0
            if helligkeit != 0:
                helligkeit = 0
            else:
                helligkeit = 255
loops.every_interval(100, on_every_interval)
