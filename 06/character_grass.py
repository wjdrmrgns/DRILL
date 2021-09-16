from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 0
count = 0
sinx = 180
cosx = 180

while True:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y + 90)
    x = 400 + 210 * math.sin(sinx / 360 * 2 * math.pi)
    y = 210 + 210 * math.cos(cosx / 360 * 2 * math.pi)
    sinx -= 5
    cosx -= 5
    delay(0.01)


close_canvas()
