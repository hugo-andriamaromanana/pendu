#Hangman using Pygame

import pygame
import random
import time

f = open('mots.txt', 'r')

content = f.read()

content = content.split('\n')
content = [i.lower() for i in content]
guess=random.choice(content)

pygame.init()

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hangman")
screen.fill(WHITE)

#fonts
font = pygame.font.SysFont('Arial', 30)
font2 = pygame.font.SysFont('Arial', 50)
font3 = pygame.font.SysFont('Arial', 20)

#text
text = font.render("Guess the word", True, BLACK)
text2 = font2.render(guess, True, BLACK)
text3 = font3.render("Press any key to start", True, BLACK)


#text position
textRect = text.get_rect()
textRect.center = (400, 50)
# textRect2 = text2.get_rect()
# textRect2.center = (400, 300)
textRect3 = text3.get_rect()
textRect3.center = (400, 550)

#blit
screen.blit(text, textRect)
# screen.blit(text2, textRect2)
screen.blit(text3, textRect3)

#update
pygame.display.update()

#reset_game
def reset_game():
    global guess
    guess_box_char=""

    guess=random.choice(content)
    pygame.display.update()

def input_box():
    global guess
    guess_box_char=""
    for i in range(len(guess)):
        guess_box_char+="_"+" "
    guess_box_char=guess_box_char[:-1]
    return guess_box_char

#game loop
running = True
while running:
    guess_box_char=input_box()
    guess_box_char=font2.render(guess_box_char, True, BLACK)
    guess_box_char_rect=guess_box_char.get_rect()
    guess_box_char_rect.center=(400, 425)
    screen.blit(guess_box_char, guess_box_char_rect)
    pygame.display.update()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_SPACE:
                reset_game()
                # text2 = font2.render(guess, True, BLACK)
                # screen.blit(text2, textRect2)
                pygame.display.update()

            if event.key == pygame.K_RETURN:
                guess=random.choice(content)
                # text2 = font2.render(guess, True, BLACK)
                # screen.blit(text2, textRect2)
                pygame.display.update()

pygame.quit()


f.close()

