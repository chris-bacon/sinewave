#!/usr/bin/python2
import pygame, sys, math, time
from pygame.locals import *

def calculateY(amp, f, speed, middle, x, width):
    # y(t) = amplitude*sin(2*pi*frequency*time + (speed * time))
    return int(middle + amp * math.sin((2 * math.pi) * f * (float(x) / width) + (speed * time.time())))

def terminate():
    pygame.quit()
    sys.exit()

def main():
    # Init
    pygame.init()
    pygame.key.set_repeat(250, 30)
    info = pygame.display.Info()
    width, height = 800, 600
    centre = (width / 2, height / 2)
    display = pygame.display.set_mode((width, height))

    # Define the size of the graph
    y_range = (40, 40)
    x_range = (width - 40, height - 40)
    graph_start = (40, height - 40) # 0-point of graph
    middle = x_range[1] - ((x_range[1] - y_range[1]) / 2) # Middle of graph

    # Values for sinewave calculation
    amplitude, frequency, speed = 50, 2, 1

    # Event loop
    while True:
        display.fill((0, 0, 0))
        # Draw x and y axis
        pygame.draw.line(display, (255, 255, 255), graph_start, x_range) # x-axis
        pygame.draw.line(display, (255, 255, 255), graph_start, y_range) # y-axis

        # Create sine wave
        for x in xrange(40, width):
            display.set_at((x, calculateY(amplitude, frequency, speed, middle, x, width)), (255, 255, 255))

        for event in pygame.event.get():
            if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                terminate()
            elif event.type == KEYDOWN and event.key == K_w:
                amplitude += 5
            elif event.type == KEYDOWN and event.key == K_s:
                amplitude -= 5
            elif event.type == KEYDOWN and event.key == K_a:
                frequency -= 0.25
            elif event.type == KEYDOWN and event.key == K_d:
                frequency += 0.25
        pygame.display.update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
