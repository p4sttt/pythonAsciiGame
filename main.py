import os
from rich.console import Console
import keyboard
import random

console = Console()

map = []


def map_generation():
    map.append(list('1' * 120))
    for j in range(21):
        line = [1]
        for i in range(118):
            if random.randint(1, 100) >= 5:
                line.append(0)
            else:
                line.append(1)
        line.append(1)
        line_str = ''.join(str(c) for c in line)
        map.append(list(line_str))
    map.append(list('1' * 120))
    return map


map_generation()


def print_map() -> None:
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                console.print(' ', end='')
            elif map[i][j] == '1':
                console.print(' ', style='white on white', end='')
            elif map[i][j] == '2':
                console.print(' ', style='white on blue', end='')
    console.print()

    console.print('tap [white on blue bold]w[/white on blue bold] to move up')
    console.print('tap [white on blue bold]a[/white on blue bold] to move left')
    console.print('tap [white on blue bold]s[/white on blue bold] to move down')
    console.print('tap [white on blue bold]d[/white on blue bold] to move right')
    console.print('or tap [white on red]q[/white on red] to leave')


class Player:
    def __init__(self):
        self.position_x = random.randint(2, len(map[0])-1)
        self.position_y = random.randint(2, len(map)-1)
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
