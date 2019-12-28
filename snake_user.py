import curses
import time
import random
import os

snake = []
screen = []
screen_size = 25
g = None
d = ''
sc = curses.initscr()


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def initialize():
    global g
    global d
    global snake
    curses.cbreak()
    curses.noecho()
    sc.keypad(True)
    sc.nodelay(1)
    g = Point(random.randint(0, screen_size - 1), random.randint(0, screen_size - 1))
    d = 'd'
    for i in range(0, screen_size + 1):
        screen.append([])

    for i in screen:
        for j in range(0, screen_size + 1):
            i.append(0)

    x = random.randint(0, screen_size - 1)
    y = random.randint(0, screen_size - 1)

    snake.append(Point(x, y))
    for i in range(1, 4):
        snake.append(Point(x, (y - i) % screen_size))
    update_screen(snake, g)


def show(s, d):
    a = '#'
    string = ''
    if d == 'w': a = '^'
    if d == 'a': a = '<'
    if d == 's': a = 'V'
    if d == 'd': a = '>'
    for i in s:
        string = string + "|"
        for j in i:
            if j == 0:
                string = string + "  "
            if j == 1:
                string = string + " #"
            if j == 2:
                string = string + " @"
            if j == 3:
                string = string + " " + a
        string = string + "|\n"
    sc.addstr(0, 0, string)


def update_screen(snake, g):
    global screen
    for i in snake:
        screen[i.x][i.y] = 1
    screen[g.x][g.y] = 2
    screen[snake[0].x][snake[0].y] = 3


def update():
    global snake
    global g
    length = len(snake)
    for i in range(1, length):
        if snake[0].x == snake[i].x and snake[0].y == snake[i].y:
            os.system('cls')
            a = '#'
            if d == 'w': a = '^'
            if d == 'a': a = '<'
            if d == 's': a = 'V'
            if d == 'd': a = '>'
            for i in screen:
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
            print('************************ GAME OVER **********************')
            exit()

    screen[snake[length - 1].x][snake[length - 1].y] = 0
    for i in range(1, length):
        j = length - i
        snake[j].x = snake[j - 1].x
        snake[j].y = snake[j - 1].y

    if d == 'd':
        snake[0].y = (snake[0].y + 1) % screen_size
    elif d == 'a':
        snake[0].y = (snake[0].y - 1) % screen_size
    elif d == 'w':
        snake[0].x = (snake[0].x - 1) % screen_size
    elif d == 's':
        snake[0].x = (snake[0].x + 1) % screen_size

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


############################   MAIN    #########################


initialize()

while True:
    update()
    sc.refresh()
    time.sleep(0.20)
    c = sc.getch()

    if c == curses.KEY_LEFT:
        if d == 'w' or d == 's':
            d = 'a'
    elif c == curses.KEY_RIGHT:
        if d == 'w' or d == 's':
            d = 'd'
    elif c == curses.KEY_UP:
        if d == 'd' or d == 'a':
            d = 'w'
    elif c == curses.KEY_DOWN:
        if d == 'a' or d == 'd':
            d = 's'
    elif c == ord('q'):
        print("Presses q")
        exit()
