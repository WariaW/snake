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
        self.lifes = 3
        self.level = 1
        self.obstacles = [[1,2], [13, 10], [12, 10], [12, 11], [14, 10]]
        self.apples = []
        self.init_state()
        self.listener = keyboard.Listener(on_press = self.on_press)
        self.listener.daemon = True
        self.listener.start()

    def init_state(self):
        self.snake_position = [[11, 0], [12, 0], [13, 0], [14, 0]]
        self.gate = []
        self.direction = 'w'
        self.listen = False
        self.board = [[' '] * self.size[1] for i in range(self.size[0])]
        for i in range(self.obstacles.__len__()):
            self.board[self.obstacles[i][0]][self.obstacles[i][1]] = 'X'
        self.apples = [([7, 7], 0), ([14, 14], 0)]
        # apple = [random.randint(self.size[0]), random.randint(self.size[1])]
        # self.apples.append(apple if apple not in (self.obstacles + self.snake_position))

    # def set_obstacles(self, obstacles):
    #     for i in range(obstacles[0].__len__()):
    #         self.board[obstacles[0][i]][obstacles[1][i]] = 'X'

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
        #print(self.apples)
        for i in range(self.apples.__len__()):
            self.board[self.apples[i][0][0]][self.apples[i][0][1]] = 'A'
        print("Level: {}, lifes: {}".format(self.level, self.lifes))
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                print("|{}".format(self.board[i][j] if [i, j] not in (self.snake_position) else 'O'), end='')
            print("|")
        print("")
        print("")

    def move(self):
        # return 0 if touch obstacle/edge
        # return 1 if eat apple
        # return 2 if reach gate to next level, level should increment by 1
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
        # Snake went out of the board
        if self.snake_position.count(self.snake_position[0]) > 1 \
                or self.snake_position[0][0] < 0 or self.snake_position[0][0] >= self.size[0] \
                or self.snake_position[0][1] < 0 or self.snake_position[0][1] >= self.size[1]:
            _ = system('cls')
            print("Looooooooser!!!")
            time.sleep(2)
            self.lifes = self.lifes - 1
            if self.lifes == 0:
                choice = 'q'
            return 0
        # snake went  into a obstacle
        if self.board[self.snake_position[0][0]][self.snake_position[0][1]] == 'X':
            _ = system('cls')
            print("Looooooooser!!!")
            time.sleep(2)
            self.lifes = self.lifes - 1
            if self.lifes == 0:
                choice = 'q'
            return 0
        # snake ate apple
        if self.board[self.snake_position[0][0]][self.snake_position[0][1]] == 'A':
            print([i for i in self.apples if i[0] == [self.snake_position[0][0], self.snake_position[0][1]]])
            print(self.apples.__len__())
            self.apples.remove([i for i in self.apples if i[0] == [self.snake_position[0][0], self.snake_position[0][1]]][0])
            self.board[self.snake_position[0][0]][self.snake_position[0][1]] = ' '
            self.snake_position.append([self.snake_position[-1][0] - (self.snake_position[-2][0] - self.snake_position[-1][0]),
                                        self.snake_position[-1][1] - (self.snake_position[-2][1] - self.snake_position[-1][1])])
        # snake reached the gate
        if self.board[self.snake_position[0][0]][self.snake_position[0][1]] == 'G':
            self.level = self.level + 1
            self.lifes = 3
            return 2
        # snake reached required length to go to the next level
        if self.snake_position.__len__() >= self.level * 1 + 8 and self.gate == []:
            self.gate = [random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)]
            while self.gate in (self.obstacles + self.snake_position):
                self.gate = [random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1)]
            self.board[self.gate[0]][self.gate[1]] = 'G'
        return 1


    def game(self):
        global choice
        self.lifes = 3
        i = 0
        while choice != 'q':
            self.init_state()
            while choice != 'q':
                _ = system('cls')
                self.print_game_board()
                self.listen = True
                time.sleep(1/2*self.level)
                self.listen = False
                if self.move() in [0, 2]:
                    # self.lifes = self.lifes - 1
                    # if self.lifes == 0:
                    #     choice = 'q'
                    break
                i += 1



if __name__== "__main__":
    snake = Snake()
    menu()
    while(choice == 'g'):
        snake.game()
        menu()
