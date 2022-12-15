import pygame
import time
import csv
from MessageClass import Message
from FruitClass import Fruit
from PlayerClass import Player
from ScoreFunction import saveScore, getHighScore

# initialisation de pygame
module_charge = pygame.init()
print(module_charge)

#variables
ecran_width = 500
ecran_height = 500
snake_block = 10
snake_speed = 6
snake_list = []
length_of_snake = 1
ecran = pygame.display.set_mode((ecran_width, ecran_height))

# couleurs
blue = (0, 0, 230)
red = (230, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)

pygame.display.set_caption("Snake by Thomas Aubert")

# récupération du meilleur score et initialisation à 0 si aucun score
hight_score = getHighScore()

# création des objets
Fruit1 = Fruit(ecran_width, ecran_height, snake_block, ecran)
Player1 = Player(blue, snake_speed, ecran_width, ecran_height, snake_block, ecran)

# horloge
clock = pygame.time.Clock()

# #boucle de jeu
loop = True

# condition de défaite
game_over = False

# boucle de jeu
while loop:
    ecran.fill((0, 0, 0))
    
    # affichage du score
    Message(str(Player1.score), (ecran_width / 20,
            ecran_height / 20), yellow).display(ecran)
    Message("High: " + str(hight_score), (ecran_width - 150, ecran_height / 20), yellow).display(ecran)

    # gestion des évènements
    Player1.handle_events()

    if (Player1.x > ecran_width or Player1.x < 0 or Player1.y > ecran_height or Player1.y < 0):
        game_over = True

    Player1.update()

    # condition de défaite
    if game_over:
        # récupération du meilleur score enregistré
        getHighScore()
    
        # enregistrement du nouveau score si meilleur score
        if Player1.score > hight_score:
            saveScore(Player1.score)

        Message("Game Over", (ecran_width / 3, ecran_height / 3), red).display(ecran)
                
        if Player1.score > hight_score:
            hight_score = Player1.score
            Message("New high score: " + str(hight_score), (ecran_width / 4, ecran_height / 2.5), green).display(ecran)
        else: 
            Message("High score: " + str(hight_score), (ecran_width / 3.3, ecran_height / 2.5), yellow).display(ecran)

        Player1.reset()

        pygame.display.update()
        time.sleep(2)
        length_of_snake = 1
        snake_speed = 6
        snake_list = []
        snake_head = []
        game_over = False

    # affichage du fruit
    Fruit1.draw()
    
    if Fruit1.color == (255, 255, 255):
        Fruit1.change()
    # affichage du serpent
    snake_head = []
    snake_head.append(Player1.x)
    snake_head.append(Player1.y)
    snake_list.append(snake_head)
    
    # gestion de la longueur du serpent
    if len(snake_list) > length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    Player1.draw(snake_list)

    # gestion de la collision avec le fruit
    if (Player1.x == Fruit1.x and Player1.y == Fruit1.y):
        Fruit1.change()
        Player1.score += 1
        length_of_snake += 1
        if Player1.score % 2 == 0:
            snake_speed += 2

    clock.tick(snake_speed)

    pygame.display.update()

pygame.quit()
quit()
