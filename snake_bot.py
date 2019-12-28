import random
import time
import os


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def show(s, d):
    os.system('cls')
    a = '#'
    if d == 'w': a = '^'
    if d == 'a': a = '<'
    if d == 's': a = 'V'
    if d == 'd': a = '>'
    for i in s:
        print("|", end="")
        for j in i:
            if j == 0:
                print("  ", end="")
            if j == 1:
                print(" #", end="")
            if j == 2:
                print(" @", end="")
            if j == 3:
                print(" " + a, end="")
        print("|")


def update_screen(snake, g):
    for i in snake:
        screen[i.x][i.y] = 1
    screen[g.x][g.y] = 2
    screen[snake[0].x][snake[0].y] = 3


def make_move(di):
    if g.x == snake[0].x and (di == 'w' or di == 's'):
        if (snake[0].y - g.y) % screen_size < (g.y - snake[0].y) % screen_size:
            return 'a'
        else:
            return 'd'
    if g.y == snake[0].y and (di == 'a' or di == 'd'):
        if (snake[0].x - g.x) % screen_size < (g.x - snake[0].x) % screen_size:
            return 'w'
        else:
            return 's'
    return di


############################   MAIN    #########################


screen_size = 25
snake = []
screen = []

flag = 0
for i in range(0, screen_size + 1):
    screen.append([])

for i in screen:
    for j in range(0, screen_size + 1):
        i.append(0)

x = random.randint(0, screen_size - 1)
y = random.randint(0, screen_size - 1)

snake.append(Point(x, y))
for i in range(1, 22):
    snake.append(Point(x, (y - i) % screen_size))
g = Point(random.randint(0, screen_size - 1), random.randint(0, screen_size - 1))
update_screen(snake, g)
d = 'd'

while True:
    d = make_move(d)
    length = len(snake)
    '''for i in snake:
        print("("+str(i.x)+","+str(i.y)+"), ", end=" ")
    print()'''

    for i in range(1, length):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            print("************ GAME OVER ************")
            exit()

    screen[snake[length - 1].x][snake[length - 1].y] = 0
    for i in range(1, length):
        j = length - i
        snake[j].x = snake[j - 1].x
        snake[j].y = snake[j - 1].y

    if d == 'd':
        snake[0].y = (snake[0].y + 1) % screen_size
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'w'
                snake[0].y = (snake[0].y - 1) % screen_size
                snake[0].x = (snake[0].x - 1) % screen_size
                break
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 's'
                snake[0].x = (snake[0].x + 2) % screen_size
                break

    elif d == 'a':
        snake[0].y = (snake[0].y - 1) % screen_size
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'w'
                snake[0].y = (snake[0].y + 1) % screen_size
                snake[0].x = (snake[0].x - 1) % screen_size
                break
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 's'
                snake[0].x = (snake[0].x + 2) % screen_size
                break

    elif d == 'w':
        snake[0].x = (snake[0].x - 1) % screen_size
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'd'
                snake[0].x = (snake[0].x + 1) % screen_size
                snake[0].y = (snake[0].y + 1) % screen_size
                break
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'a'
                snake[0].y = (snake[0].y - 2) % screen_size
                break

    elif d == 's':
        snake[0].x = (snake[0].x + 1) % screen_size
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'd'
                snake[0].x = (snake[0].x - 1) % screen_size
                snake[0].y = (snake[0].y + 1) % screen_size
                break
        for i in range(1, length):
            if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
                d = 'a'
                snake[0].y = (snake[0].y - 2) % screen_size
                break

    if g.x == snake[0].x and g.y == snake[0].y:
        length = len(snake)
        snake.append(Point(snake[length - 1].x, snake[length - 1].y))
        length = len(snake)
        g = Point(random.randint(0, screen_size - 1), random.randint(0, screen_size - 1))
        i = 0
        while i < length:
            if g.x == snake[i].x and g.y == snake[i].y:
                g = Point(random.randint(0, screen_size - 1), random.randint(0, screen_size - 1))
                i = -1
            i = i + 1

    update_screen(snake, g)
    show(screen, d)
    time.sleep(0.06)
