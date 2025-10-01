import os
import sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' 
import pygame 
import numpy as np
import algorithems

# Initialize Pygame
pygame.init()

def check_keyboard():
    global running
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def draw(arr, j):
    check_keyboard()

    # Drawing
    screen.fill(BLACK)  # Fill the background

    arr_length = len(arr)
    height_const = 300
    min_arr = min(arr)
    max_arr = max(arr)
    for i in range(arr_length):
        normilze_arr = ((arr[i] - min_arr) / (max_arr - min_arr)) * (1 - 0.1) + 0.1

        if i == j:
            color = (0,255,0)
        elif i == j+1:
            color = (0,0,255)
        else:
            color = [normilze_arr*100+155]*3

        height_length = (HEIGHT-height_const)*normilze_arr

        pygame.draw.rect(screen, color,  (WIDTH/arr_length*i,   HEIGHT-height_length, 
                                                                WIDTH/arr_length, height_length))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)


# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting algorithems")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game loop variables
running = True
clock = pygame.time.Clock()
FPS = 10

arr = np.random.randint(0, 100, 10)
np_sort = np.sort(arr)
my_sort = algorithems.bubble_sort(arr, draw=draw)


# Game loop
while running:
    pass



# Quit Pygame
pygame.quit()