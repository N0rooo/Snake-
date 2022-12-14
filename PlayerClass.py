import pygame

class Player:
    def __init__(self, color, snake_speed, ecran_width, ecran_height, snake_block, screen):
        self.x = 250
        self.y = 250
        self.x2 = 0
        self.y2 = 0
        self.color = color
        self.snake_speed = snake_speed
        self.ecran_width = ecran_width
        self.ecran_height = ecran_height
        self.snake_block = snake_block
        self.screen = screen
        self.loop = True
        self.score = 0
        
        
    def draw(self, snakeList):
        for i in snakeList:
            pygame.draw.rect(self.screen, self.color, [i[0], i[1], self.snake_block, self.snake_block])
            

        
    def handle_events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    self.loop = False
                elif event.key == pygame.K_LEFT:
                    self.x2 = -self.snake_block
                    self.y2 = 0
                elif event.key == pygame.K_RIGHT:
                    self.x2 = self.snake_block
                    self.y2 = 0
                elif event.key == pygame.K_UP:
                    self.x2 = 0
                    self.y2 = -self.snake_block
                elif event.key == pygame.K_DOWN:
                    self.x2 = 0
                    self.y2 = self.snake_block

            if event.type == pygame.QUIT:
                self.loop = False
                
    def update(self):
        self.x += self.x2
        self.y += self.y2
        
    def reset(self):
        self.x = 250
        self.y = 250
        self.x2 = 0
        self.y2 = 0
        self.score = 0
        self.snake_speed = 6
        
        
