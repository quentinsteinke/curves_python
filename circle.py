import pygame
from functions import tupleSub


class Circle():
    instances = []

    def __init__(self, name: str, screen, color, x, y, size):
        self.instances.append(self)
        self.name = name
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.size = size
        self.position = (x, y)
        

    def transform(self, position):
        self.position = position
        self.x = self.position[0]
        self.y = self.position[1]


    def x_pos(self, pos):
        self.x = pos
        self.position = (self.x, self.y)

    
    def y_pos(self, pos):
        self.y = pos
        self.position = (self.x, self.y)
    
    
    def on_clicked(self, mouse_pos):
        self.transform(tupleSub(mouse_pos, tupleSub(mouse_pos, self.position)))


    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)
    