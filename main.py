#Hangman using Pygame

import pygame
import random
import time

#open the file
f = open('mots.txt', 'r')
#read the file
content = f.read()
#Make the file a list
content = content.split('\n')
content = [i.lower() for i in content]

#initialize pygame
pygame.init()

#variables
guess=random.choice(content)
guess_box_char=""
guess_letter_list=[]
tries=0
user_input_letter=""

#---------------------Functions---------------------

def check_letter(letter):
    global guess
    global guess_letter_list
    global guess_box_char
    global tries
    global user_input_letter
    if letter in guess:
        for i in range(len(guess)):
            if letter==guess[i]:
                guess_letter_list[i]=letter
        guess_box_char=""
        for i in range(len(guess_letter_list)):
            guess_box_char+=guess_letter_list[i]+" "
        guess_box_char=guess_box_char[:-1]
        draw_word(guess_box_char)
        if guess_box_char.replace(" ","")==guess:
            text2 = font2.render("You win", True, BLACK)
            textRect2 = text2.get_rect()
            textRect2.center = (400, 225)
            screen.blit(text2, textRect2)
            pygame.display.update()
            time.sleep(2)
            reset_game()
    else:
        tries+=1
        if tries==1:
            pygame.draw.line(screen, BLACK, (200, 250), (600, 250), 2)
        elif tries==2:
            pygame.draw.line(screen, BLACK, (200, 250), (200, 500), 2)
        elif tries==3:
            pygame.draw.line(screen, BLACK, (200, 500), (400, 500), 2)
        elif tries==4:
            pygame.draw.line(screen, BLACK, (400, 500), (400, 450), 2)
        elif tries==5:
            pygame.draw.circle(screen, BLACK, (400, 475), 25, 2)
        elif tries==6:
            pygame.draw.line(screen, BLACK, (400, 500), (400, 550), 2)
        elif tries==7:
            pygame.draw.line(screen, BLACK, (400, 550), (375, 575), 2)
        elif tries==8:
            pygame.draw.line(screen, BLACK, (400, 550), (425, 575), 2)
        elif tries==9:
            pygame.draw.line(screen, BLACK, (400, 500), (375, 525), 2)
        elif tries==10:
            pygame.draw.line(screen, BLACK, (400, 500), (425, 525), 2)
            text2 = font2.render("You lose", True, BLACK)
            textRect2 = text2.get_rect()
            textRect2.center = (400, 225)
            screen.blit(text2, textRect2)
            pygame.display.update()

            time.sleep(2)
            reset_game()

def draw_word(guess_box_char):
    global guess
    global guess_letter_list
    global guess_box_char
    global tries
    global user_input_letter
    text2 = font2.render(guess_box_char, True, BLACK)
    textRect2 = text2.get_rect()
    textRect2.center = (400, 225)
    screen.blit(text2, textRect2)
    pygame.display.update()

def reset_game():
    global guess
    global guess_letter_list
    global guess_box_char
    global tries
    global user_input_letter
    guess_letter_list=[]
    guess_box_char=""
    tries=0
    guess=random.choice(content)
    pygame.display.update()
    for i in range(len(guess)):
        guess_letter_list.append("_")
    guess_box_char=input_box()
    draw_word(guess_box_char)

def input_box():
    global guess
    global guess_letter_list
    global guess_box_char
    global tries
    global user_input_letter
    guess_box_char=""
    for i in range(len(guess_letter_list)):
        guess_box_char+=guess_letter_list[i]+" "
    guess_box_char=guess_box_char[:-1]
    return guess_box_char

#---------------------Main---------------------



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


#Square for the word
pygame.draw.rect(screen, BLACK, (200, 200, 400, 50), 2)


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
    pygame.display.update()
    for i in range(len(guess)):
        guess_box_char+="_"+" "
    guess_box_char=guess_box_char[:-1]
    return guess_box_char

#Draw the hangman
def draw_hangman():
    pygame.draw.line(screen, BLACK, (200, 250), (600, 250), 2)
    pygame.draw.line(screen, BLACK, (200, 250), (200, 500), 2)
    pygame.draw.line(screen, BLACK, (200, 500), (400, 500), 2)
    pygame.draw.line(screen, BLACK, (400, 500), (400, 450), 2)
    pygame.draw.circle(screen, BLACK, (400, 475), 25, 2)
    pygame.draw.line(screen, BLACK, (400, 500), (400, 550), 2)
    pygame.draw.line(screen, BLACK, (400, 550), (375, 575), 2)
    pygame.draw.line(screen, BLACK, (400, 550), (425, 575), 2)
    pygame.draw.line(screen, BLACK, (400, 500), (375, 525), 2)
    pygame.draw.line(screen, BLACK, (400, 500), (425, 525), 2)

#Draw the word
def draw_word(guess_box_char):
    global guess
    text2 = font2.render(guess_box_char, True, BLACK)
    textRect2 = text2.get_rect()
    textRect2.center = (400, 225)
    screen.blit(text2, textRect2)
    pygame.display.update()

#Draw the letter
def draw_letter(letter):
    global guess
    text2 = font2.render(letter, True, BLACK)
    textRect2 = text2.get_rect()
    textRect2.center = (400, 225)
    screen.blit(text2, textRect2)
    pygame.display.update()

#game loop
running = True
f.close()

