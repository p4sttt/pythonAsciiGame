import os
import random

WIDTH = 120
HEIGHT = 30
WIDTH_MAP = WIDTH
HEIGHT_MAP = HEIGHT - 4

map_list = []


def map_generation():
    map_list.append(list('9' * WIDTH_MAP))
    for j in range(HEIGHT_MAP - 2):
        line = ['9']
        for i in range(WIDTH_MAP - 2):
            if random.randint(1, 100) >= 5:
                line.append('0')
            elif random.randint(1, 100) >= 15:
                line.append('1')
            else:
                line.append('9')
        line.append('9')
        map_list.append(line)
    map_list.append(list('9' * WIDTH_MAP))
    return map_list


map_generation()


def print_map() -> None:
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == '9':
                print('#', end='')
            elif map_list[i][j] == '1':
                print('.', end='')
            elif map_list[i][j] == '2':
                print('@', end='')
            else:
                print(' ', end='')
        print()
    print('type  up down left right  to move')
    print('or type  quit  to leave')


print_map()


class Player:
    def __init__(self):
        self.position_x = random.randint(2, len(map_list[0]) - 2)
        self.position_y = random.randint(2, len(map_list) - 2)
        map_list[self.position_y][self.position_x] = '2'
        self.level = 2
        os.system('cls')
        print_map()
        print(self.level)

    def level_print(self):
        print(self.level)

    def move_up(self):
        if int(map_list[self.position_y - 1][self.position_x]) < self.level and map_list[self.position_y - 1][self.position_x] != '9':
            self.level += int(map_list[self.position_y - 1][self.position_x])
            map_list[self.position_y][self.position_x] = '0'
            self.position_y -= 1
            map_list[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()
        self.level_print()

    def move_down(self):
        if int(map_list[self.position_y + 1][self.position_x]) < self.level and map_list[self.position_y + 1][self.position_x] != '9':
            self.level += int(map_list[self.position_y + 1][self.position_x])
            map_list[self.position_y][self.position_x] = '0'
            self.position_y += 1
            map_list[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()
        self.level_print()

    def move_right(self):
        if int(map_list[self.position_y][self.position_x + 1]) < self.level and map_list[self.position_y][self.position_x + 1] != '9':
            self.level += int(map_list[self.position_y][self.position_x + 1])
            map_list[self.position_y][self.position_x] = '0'
            self.position_x += 1
            map_list[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()
        self.level_print()

    def move_left(self):
        if int(map_list[self.position_y][self.position_x - 1]) < self.level and map_list[self.position_y][self.position_x - 1] != '9':
            self.level += int(map_list[self.position_y][self.position_x - 1])
            map_list[self.position_y][self.position_x] = '0'
            self.position_x -= 1
            map_list[self.position_y][self.position_x] = '2'
        os.system('cls')
        print_map()
        self.level_print()


player = Player()


while True and player.level != 20:
    key = input()
    if key == 'up':
        player.move_up()
    elif key == 'down':
        player.move_down()
    elif key == 'right':
        player.move_right()
    elif key == 'left':
        player.move_left()
    elif key == 'quit':
        break
    else:
        os.system('cls')
        print_map()

print('                              .__        ')
print(' ___.__. ____  __ __  __  _  _|__| ____  ')
print('<   |  |/  _ \|  |  \ \ \/ \/ /  |/    \ ')
print(' \___  (  <_> )  |  /  \     /|  |   |  \\')
print(' / ____|\____/|____/    \/\_/ |__|___|  /')
print(' / ____|\____/|____/    \/\_/ |__|___|  /')
