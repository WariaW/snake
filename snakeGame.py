import time
from os import system
from pynput import keyboard
import random

choice = ''
def menu():
    global choice
    print("~~~~~~~~~~~~SNAKE~~~~~~~~~~~~")
    print('Enter g to play or any other key to quit')
    print('Press Esc on keyboard during game to end')
    choice = input('')


class Snake():

    def __init__(self):
        self.size = (15, 20)
        self.board = [[' '] * self.size[1] for i in range(self.size[0])]
        self.level = 2
        self.init_state()
        self.listener = keyboard.Listener(on_press = self.on_press)
        self.listener.start()

    def init_state(self):
        self.snake_position = [[11, 0], [12, 0], [13, 0], [14, 0]]
        self.direction = 'w'
        self.listen = False
        if self.level > 1:
            obs = [random.sample(range(self.size[0]), self.level * 2), random.sample(range(self.size[1]), self.level * 2)]
            self.set_obstacles(obs)


    def set_obstacles(self, obstacles):
        for i in range(obstacles[0].__len__()):
            self.board[obstacles[0][i]][obstacles[1][i]] = 'X'

    def on_press(self, key):
        global choice
        if key == keyboard.Key.esc:
            choice = 'q'
        elif self.listen == True:
            if key.char in ['w', 's'] and self.direction in ['a', 'd']:
                self.direction = key.char
                self.listen = False
            if key.char in ['a', 'd'] and self.direction in ['w', 's']:
                self.direction = key.char
                self.listen = False

    def print_game_board(self):
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                print("|{}".format(self.board[i][j] if [i, j] not in self.snake_position else 'O'), end='')
            print("|")
        print("")
        print("")

    def move(self):
        global choice
        for i in range(self.snake_position.__len__() - 1, 0, -1):
            self.snake_position[i] = self.snake_position[i - 1]
        if self.direction == 'w':
            self.snake_position[0] = [self.snake_position[0][0] - 1, self.snake_position[0][1]]
        elif self.direction == 'd':
            self.snake_position[0] = [self.snake_position[0][0], self.snake_position[0][1] + 1]
        elif self.direction == 's':
            self.snake_position[0] = [self.snake_position[0][0] + 1, self.snake_position[0][1]]
        elif self.direction == 'a':
            self.snake_position[0] = [self.snake_position[0][0], self.snake_position[0][1] - 1]
        if self.snake_position.count(self.snake_position[0]) > 1 \
                or self.snake_position[0][0] < 0 or self.snake_position[0][0] > self.size[0] \
                or self.snake_position[0][1] < 0 or self.snake_position[0][1] > self.size[0]\
                or self.board[self.snake_position[0][0]][self.snake_position[0][1]] == 'X':
            _ = system('cls')
            print("Looooooooser!!!")
            time.sleep(2)
            return False
        return True


    def game(self):
        global choice
        self.lifes = 3
        i = 0
        while self.lifes > 0  and choice != 'q':
            self.init_state()
            while choice != 'q':
                _ = system('cls')
                self.print_game_board()
                self.listen = True
                time.sleep(1/self.level)
                self.listen = False
                if not self.move():
                    self.lifes = self.lifes - 1
                    break
                i += 1



if __name__== "__main__":
    snake = Snake()
    menu()
    while(choice == 'g'):
        snake.game()
        menu()
