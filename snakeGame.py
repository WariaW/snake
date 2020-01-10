import time
from os import system
from pynput import keyboard

class Snake():
    def __init__(self):
        self.size = (15, 20)
        self.board = [[' '] * self.size[1] for i in range(self.size[0])]
        self.snake_position = [[2, 0], [3, 0], [4, 0], [5, 0]]
        self.direction = 'd'

    def on_press(self, key):
        if key in ['w', 'a', 's', 'd']:
            self.direction = key

    # Collect events until released
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    #     listener.join()

    def print_game_board(self):
        for i in range(0, self.size[0]):
            for j in range(0, self.size[1]):
                print(' -', end='')
            print("")
            for j in range(0, self.size[1]):
                print("|{}".format(' ' if [i, j] not in self.snake_position else u"\u25AE"), end='')
            print("|")
        for i in range(0, self.size[1]):
            print(' -', end='')
        print("")


    def move(self):
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

    def game(self):
        i = 0
        while(i < 15):
            _ = system('cls')
            self.print_game_board()
            time.sleep(0.5)
            self.move()

            i += 1

if __name__== "__main__":
    snake = Snake()
    snake.game()