from pico2d import *
import random

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,500), 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0,1000), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y -= random.randint(0,10)

    def draw(self):
        self.image.clip_draw(self.frame*100,0,21,21,self.x,self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0,1100), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')

    def update(self):
        self.frame = (self.frame + 1) % 1
        self.y -= random.randint(0,20)

    def draw(self):
        self.image.clip_draw(self.frame*100,0,42,42,self.x,self.y)
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
team = [Boy() for i in range(11)]
balls = [SmallBall() for i in range(20)]
Balls = [BigBall() for i in range(20)]
# boy = Boy()
grass = Grass()

running = True


# game main loop code
while running:
    handle_events()

    # boy.update()
    for boy in team:
        boy.update()
    for small in balls:
        small.update()
    for big in Balls:
        big.update()
    clear_canvas()
    grass.draw()
    # boy.draw()
    for boy in team:
        boy.draw()
    for small in balls:
        small.draw()
    for Big in Balls:
        Big.draw()
    update_canvas()

    delay(0.05)

# finalization code
