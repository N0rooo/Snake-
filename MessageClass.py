import pygame

class Message:
    def __init__(self, text, position, color):
        self.text = text
        self.position = position
        self.color = color

    def display(self, ecran):
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(self.text, True, self.color)
        ecran.blit(text, self.position)