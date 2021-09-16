from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

count = 0

x = 400
y = 0
sinx = 180
cosx = 180


while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y + 90)
    if count == 0:
        if y == 0 and x < 800:
            if x == 395:
                sinx = 180
                cosx = 180
                count = 1
            x += 5
            delay(0.01)
        elif x == 800 and y < 465:
            y += 5
            delay(0.01)
        elif y == 465 and x > 0:
            x -= 5
            delay(0.01)
        else:
            y -= 5
            delay(0.01)

    else:
        x = 400 + 210 * math.sin(sinx / 360 * 2 * math.pi)
        y = 210 + 210 * math.cos(cosx / 360 * 2 * math.pi)
        sinx -= 1
        cosx -= 1
        if sinx == -180:
            x = 400
            y = 0
            count = 0
        delay(0.01)

        
close_canvas()
