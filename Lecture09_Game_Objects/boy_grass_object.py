from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자를 이용해서 객체의 초기 상태를 정의
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

class Ball:
    def __init__(self, image_name, size, speed):
        self.x = random.randint(0, 800)
        self.y = 599
        self.image = load_image(image_name)
        self.size = size
        self.speed = speed

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.speed

        if self.size == 41:
            if self.y <= 76:
                self.speed = 0
        else:
            if self.y <= 65:
                self.speed = 0


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def reset_world():  # 초기화하는 함수
    global running
    global grass
    global team
    global world
    global balls

    running = True
    world = []

    grass = Grass() # Grass 클래스를 이용해서 grass 객체 생성
    world.append(grass)

    team = [Boy() for i in range(10)]
    world += team

    balls = []
    for i in range(20):
        choice = random.randint(0,1)
        if choice == 0:
            image_name = 'ball21x21.png'
            size = 21
            speed = 3 * (i + 1) / 5
            #speed = random.randint(1,20)
        else:
            image_name = 'ball41x41.png'
            size = 41
            speed = 3 * (i + 1) / 5
            #speed = random.randint(1,20)

        balls.append(Ball(image_name, size, speed))
    world += balls

open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
