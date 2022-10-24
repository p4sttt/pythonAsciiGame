import os
from rich.console import Console
from rich.progress import track
import keyboard
import random
import time

WIDTH = 120
HEIGHT = 30

console = Console(width=WIDTH, height=HEIGHT)

map = []


def print_hello():
    os.system('cls')
    console.print('                     .__.__                  .__   __                 ')
    console.print('_____    ______ ____ |__|__| __  _  _______  |  | |  | __ ___________ ')
    console.print('\__  \  /  ___// ___\|  |  | \ \/ \/ /\__  \ |  | |  |/ // __ \_  __ \\')
    console.print(' / __ \_\___ \\\\  \___|  |  |  \     /  / __ \|  |_|    <\  ___/|  | \/')
    console.print('(____  /____  >\___  >__|__|   \/\_/  (____  /____/__|_ \\\___  >__|   ')
    console.print('     \/     \/     \/                      \/          \/    \/       ')
    print()
    print()
    for _ in track(range(100), description='[green]Loading...'):
        time.sleep(0.02)


print_hello()


def map_generation():
    map.append(list('1' * WIDTH))
    for j in range(HEIGHT - 5):
        line = [1]
        for i in range(WIDTH - 2):
            if random.randint(1, 100) >= 5:
                line.append(0)
            else:
                line.append(1)
        line.append(1)
        line_str = ''.join(str(c) for c in line)
        map.append(list(line_str))
    map.append(list('1' * WIDTH))
    return map


map_generation()


def print_map() -> None:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                console.print(' ', end='')
            elif map[i][j] == '1':
                console.print('@', end='')
            elif map[i][j] == '2':
                console.print(' ', style='white on blue', end='')
    console.print()

    console.print('use [white on blue] w a s d [/white on blue] to move')
    console.print('or tap [white on red] q [/white on red] to leave')


class Player:
    def __init__(self):
        self.position_x = random.randint(2, len(map[0])-2)
        self.position_y = random.randint(2, len(map)-2)
        map[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()

    def move_up(self):
        if map[self.position_y - 1][self.position_x] != '1':
            map[self.position_y][self.position_x] = '0'
            self.position_y -= 1
            map[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()

    def move_down(self):
        if map[self.position_y + 1][self.position_x] != '1':
            map[self.position_y][self.position_x] = '0'
            self.position_y += 1
            map[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()
        
    def move_right(self):
        if map[self.position_y][self.position_x + 1] != '1':
            map[self.position_y][self.position_x] = '0'
            self.position_x += 1
            map[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()

    def move_left(self):
        if map[self.position_y][self.position_x - 1] != '1':
            map[self.position_y][self.position_x] = '0'
            self.position_x -= 1
            map[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()


player = Player()


while True:
    key = keyboard.read_key()
    if key == 'w':
        player.move_up()
    elif key == 's':
        player.move_down()
    elif key == 'd':
        player.move_right()
    elif key == 'a':
        player.move_left()
    else:
        break
