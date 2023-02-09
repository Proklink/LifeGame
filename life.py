import pygame
import random, time, math

WIDTH = 360 *2
HEIGHT = 480
FPS = 20

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RR = (255, 0, 255)
RD = (0, 196, 255)
RP = (255, 0, 128)
ASD = (188, 196, 96)
ASD1 = (188, 0, 96)

colors_live = [WHITE]
colors_dead = [BLACK]

rect_width = 10
rect_height = 10

W = int(WIDTH / rect_width) #36
H = int(HEIGHT / rect_height) #48

screen = []
random.seed(int(time.time()))

def init():
    for y in range(H):
        for x in range(W):
            rect = pygame.Rect(x * rect_width, y * rect_height, rect_width, rect_height)
            mas = [0, rect]
            
            r = random.randint(1, 2000)
            _x = random.randint(0, 1)
            _y = not _x
            if r > random.randint(1, r) and r < random.randint(r, 2000):
                if x % 2 == _x and y % 2 == _y:
                    mas[0] = random.randint(0, 1)
            screen.append(mas)


def pixel(x, y):
    return screen[y * W + x][1]

def value(x, y):
    if x < 0 or y < 0 or x >= W or y >= H:
        return 0

    return screen[y * W + x][0]

def set_value(x, y, val):
    screen[y * W + x][0] = val

def dead(x, y):
    if value(x - 1, y - 1) + value(x - 1, y) + value(x - 1, y + 1) + \
       value(x, y - 1) + value(x, y + 1) + value(x + 1, y - 1) + \
       value(x + 1, y) + value(x + 1, y + 1) == 3:
        set_value(x, y, 1)

def alive(x, y):
    val = value(x - 1, y - 1) + value(x - 1, y) + value(x - 1, y + 1) + \
          value(x, y - 1) + value(x, y + 1) + value(x + 1, y - 1) + \
          value(x + 1, y) + value(x + 1, y + 1)
    if val < 2 or val > 3:
        set_value(x, y, 0)

def update():
    for y in range(H):
        for x in range(W):
            if value(x, y) == 0:
                dead(x, y)
            else:
                alive(x, y)
            
def render(window):
    for y in range(H):
        for x in range(W):
            if value(x, y) == 0:
                window.fill(colors_dead[random.randint(0, len(colors_dead) - 1)], pixel(x, y))
            else:
                window.fill(colors_live[random.randint(0, len(colors_live) - 1)], pixel(x, y))

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    update()
    # Рендеринг
    window.fill(BLACK)
    render(window)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()