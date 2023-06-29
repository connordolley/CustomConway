import pygame
import numpy as np
import random

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 60, 60
SQUARE_SIZE = WIDTH//COLS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self, rows, cols, min_live, max_live):
        self.rows = rows
        self.cols = cols
        self.grid = np.random.choice([0,1], size=(rows, cols))
        self.min_live = min_live
        self.max_live = max_live

    def draw_grid(self, win):
        for i in range(ROWS):
            for j in range(COLS):
                pygame.draw.rect(win, WHITE, (i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
                if self.grid[i, j] == 1:
                    pygame.draw.rect(win, WHITE, (i*SQUARE_SIZE, j*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def update(self):
        newGrid = self.grid.copy()
        for i in range(self.rows):
            for j in range(self.cols):
                total = (self.grid[(i-1)%ROWS, (j-1)%COLS] + self.grid[(i-1)%ROWS, j] + self.grid[(i-1)%ROWS, (j+1)%COLS] +
                         self.grid[i, (j-1)%COLS] + self.grid[i, (j+1)%COLS] +
                         self.grid[(i+1)%ROWS, (j-1)%COLS] + self.grid[(i+1)%ROWS, j] + self.grid[(i+1)%ROWS, (j+1)%COLS])
                if self.grid[i, j]  == 1:
                    if (total < self.min_live) or (total > (self.max_live)):
                        newGrid[i, j] = 0
                else:
                    if total == 3:
                        newGrid[i, j] = 1

        self.grid = newGrid


def main(min_live, max_live):
    run = True
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game(ROWS, COLS, min_live, max_live)

    while run:
        clock.tick(10)
        game.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        win.fill(BLACK)
        game.draw_grid(win)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    print("Configuration")
    min_live = int(input("Minium amount of alive neighbors required for cell to survive: "))
    max_live = int(input("The maximum amount of alive neighbors for cell to survive: "))
    
    main(min_live, max_live)
