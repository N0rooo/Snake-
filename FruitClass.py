import pygame
import random

class Fruit:
    def __init__(self, ecran_width, ecran_height, snake_block, screen):
        self.x = round(random.randrange(0, ecran_width - snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, ecran_height - snake_block) / 10.0) * 10.0  
        self.ecran_width = ecran_width
        self.ecran_height = ecran_height   
        self.snake_block = snake_block 
        self.screen = screen
        self.color = round(random.randrange(0, 255)), round(random.randrange(0, 255)), round(random.randrange(0, 255))
        
        
    def change(self):
        self.x = round(random.randrange(0, self.ecran_width - self.snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.ecran_height - self.snake_block) / 10.0) * 10.0
        self.color = round(random.randrange(0, 255)), round(random.randrange(0, 255)), round(random.randrange(0, 255))

        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.snake_block, self.snake_block])
