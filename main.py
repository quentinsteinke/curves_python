from turtle import position
import pygame
from pygame.locals import MOUSEMOTION


# Variables
white = (200, 200, 200)
black = (0, 0, 0)
red = (210, 50, 50)
green = (80, 160, 80)
blue = (50, 50, 210)

screen_width = 1440
screen_height = 720

fps = 60

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

# Program loop
running = True
while running:

    pygame.time.Clock().tick(fps)

    # Event triggers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
                
        if event.type == pygame.K_ESCAPE:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    mouse_pos = pygame.mouse.get_pos()

    screen.fill(white)


    # Creating points
    t = 0.25

    p1 = pygame.draw.circle(screen, green, (screen_width - 20, screen_height/2), 10)

    p2 = pygame.draw.circle(screen, red, (mouse_pos[0], mouse_pos[1]), 10)


    # Linear interpolation
    # Formula - p1 * (1 - t) + p2 * t
    def lerp(p1, p2, t):
        p1 = tuple((1 - t) * i for i in p1)
        p2 = tuple(t * i for i in p2)

        position = (p1[0] + p2[0], p1[1] + p2[1])

        return position

    p3_pos = lerp(p1.center, p2.center, t)


    print(p3_pos)
    p3 = pygame.draw.circle(screen, blue, (p3_pos), 10)


    pygame.display.update()


pygame.quit()