import pygame
import random
import time
import json
import sys
#---------------------Setup---------------------

#---------------------Importing Files-----------

#---------------------Importing txt-----------
f = open('mots.txt', 'r')
content = f.read()
content = content.split('\n')
content=content[1:]
content = [i.lower() for i in content]
#---------------------Importing Json-----------

with open("scoreboard.json","r") as f:
    scoreboard = json.load(f)


#---------------------Constantes---------------------
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
MODE={
    "Easy":{
        "MAX_TIME":180,
        "MAX_ERRORS":6
    },
    "Medium":{
        "MAX_TIME":120,
        "MAX_ERRORS":4
    },
    "Hard":{
        "MAX_TIME":60,
        "MAX_ERRORS":2
    }
}
AUTHORIZED_KEYS = "abcdefghijklmnopqrstuvwxyz"

#---------------------Variables---------------------
score=0
errors=0
time_left=0
input_letter=''
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
easy_scoreboard=""
medium_scoreboard=""
hard_scoreboard=""
gamemode="Easy"
game_over=False
easy_scoreboard_data=scoreboard[([i for i in scoreboard])[0]]
medium_scoreboard_data=scoreboard[([i for i in scoreboard])[1]]
hard_scoreboard_data=scoreboard[([i for i in scoreboard])[2]]
name=""
running=True
#---------------------Functions----------------------------

def sort_scoreboard_data_by_score():
    global easy_scoreboard_data
    global medium_scoreboard_data
    global hard_scoreboard_data
    easy_scoreboard_data=dict(sorted(easy_scoreboard_data.items(), key=lambda x: x[1], reverse=True))
    medium_scoreboard_data=dict(sorted(medium_scoreboard_data.items(), key=lambda x: x[1], reverse=True))
    hard_scoreboard_data=dict(sorted(hard_scoreboard_data.items(), key=lambda x: x[1], reverse=True))


def score_calculate(elapsed_time,errors_left):
    return int(1000*(errors_left/elapsed_time))

def get_all_index_to_replace():
    global word_to_guess
    global input_letter
    if input_letter in word_to_guess:
        index_arr=[]
        count=0
        for i in word_to_guess:
            if i == input_letter:
                index_arr.append(count)
            count+=1
    return index_arr

def display_matching_letters():
    global word_to_guess_display
    global input_letter
    for i in get_all_index_to_replace():
        word_to_guess_display[i]=input_letter
    input_letter=''

def play_again():
    global word_to_guess
    global word_to_guess_display
    global score
    global errors
    global time_left
    global game_over
    global gamemode
    word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
    word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
    score=0
    errors=0
    time_left=0
    game_over=False
    gamemode=""#current gamemode

def get_3_best(dic):
    arr=[]
    for i in dic:
        arr.append(f'{i} : {dic[i]}')
    return arr[:3]


# #---------------------Pygame---------------------
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1500, 600))
screen.fill(WHITE)

#---------------------Main Menu---------------------


COMIC_SANS= pygame.font.SysFont('Comic Sans MS', 30)

#Hard button
hard_button_rect = pygame.Rect(650, 100, 120, 50)
hard_button_text = COMIC_SANS.render("Hard", True, BLACK)
hard_button_rect_center=hard_button_text.get_rect(center=hard_button_rect.center)
#Medium button
medium_button_rect = pygame.Rect(650, 200, 120, 50)
medium_button_text = COMIC_SANS.render("Medium", True, BLACK)
medium_button_rect_center=medium_button_text.get_rect(center=medium_button_rect.center)
#Easy button
easy_button_rect = pygame.Rect(650, 300, 120, 50)
easy_button_text = COMIC_SANS.render("Easy", True, BLACK)
easy_button_rect_center=easy_button_text.get_rect(center=easy_button_rect.center)
#Exit button
exit_button_rect = pygame.Rect(650, 400, 120, 50)
exit_button_text = COMIC_SANS.render("Exit", True, WHITE)
exit_button_rect_center=exit_button_text.get_rect(center=exit_button_rect.center)
#Scoreboard button
scoreboard_button_rect = pygame.Rect(300, 10, 160, 50)
scoreboard_button_text = COMIC_SANS.render("Scoreboard", True, BLACK)
scoreboard_button_rect_center=scoreboard_button_text.get_rect(center=scoreboard_button_rect.center)
#Scoreboard popup window
scoreboard_popup=pygame.display.set_mode((1000, 650))
scoreboard_popup.fill(WHITE)
#Scoreboard popup window exit button
scoreboard_popup_exit_button_rect = pygame.Rect(700,10, 50, 50)
scoreboard_popup_exit_button_text = COMIC_SANS.render("X", True, WHITE)
scoreboard_popup_exit_button_rect_center=scoreboard_popup_exit_button_text.get_rect(center=scoreboard_popup_exit_button_rect.center)
            
state="main_menu"

def game_state(state):
    if state=="main_menu":
        pygame.draw.rect(screen, RED, exit_button_rect)
        screen.blit(exit_button_text, exit_button_rect_center)
        pygame.draw.rect(screen, GREEN, hard_button_rect)
        screen.blit(hard_button_text, hard_button_rect_center)
        pygame.draw.rect(screen, YELLOW, medium_button_rect)
        screen.blit(medium_button_text, medium_button_rect_center)
        pygame.draw.rect(screen, BLUE, easy_button_rect)
        screen.blit(easy_button_text, easy_button_rect_center)
        pygame.draw.rect(screen, BLACK, scoreboard_button_rect)
        screen.blit(scoreboard_button_text, scoreboard_button_rect_center)
    elif state=="scoreboard":
        pygame.draw.rect(scoreboard_popup, RED, scoreboard_popup_exit_button_rect)
        scoreboard_popup.blit(scoreboard_popup_exit_button_text, scoreboard_popup_exit_button_rect_center)
        scoreboard_popup.blit(COMIC_SANS.render("SCOREBOARD", True, YELLOW), (400, 10))
        scoreboard_popup.blit(COMIC_SANS.render("Easy", True, GREEN), (100, 100))
        scoreboard_popup.blit(COMIC_SANS.render("Medium", True, BLUE), (450, 100))
        scoreboard_popup.blit(COMIC_SANS.render("Hard", True, RED), (800, 100))
        scoreboard_popup.blit(COMIC_SANS.render("1st "+get_3_best(easy_scoreboard_data)[0], True, BLACK), (20, 200))
        scoreboard_popup.blit(COMIC_SANS.render("2nd "+get_3_best(easy_scoreboard_data)[1], True, BLACK), (20, 300))
        scoreboard_popup.blit(COMIC_SANS.render("3rd "+get_3_best(easy_scoreboard_data)[2], True, BLACK), (20, 400))
        scoreboard_popup.blit(COMIC_SANS.render("1st "+get_3_best(medium_scoreboard_data)[0], True, BLACK), (370, 200))
        scoreboard_popup.blit(COMIC_SANS.render("2nd "+get_3_best(medium_scoreboard_data)[1], True, BLACK), (370, 300))
        scoreboard_popup.blit(COMIC_SANS.render("3rd "+get_3_best(medium_scoreboard_data)[2], True, BLACK), (370, 400))
        scoreboard_popup.blit(COMIC_SANS.render("1st "+get_3_best(hard_scoreboard_data)[0], True, BLACK), (720, 200))
        scoreboard_popup.blit(COMIC_SANS.render("2nd "+get_3_best(hard_scoreboard_data)[1], True, BLACK), (720, 300))
        scoreboard_popup.blit(COMIC_SANS.render("3rd "+get_3_best(hard_scoreboard_data)[2], True, BLACK), (720, 400))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state=="main_menu":
                if exit_button_rect.collidepoint(event.pos):
                    running=False
                elif hard_button_rect.collidepoint(event.pos):
                    state="hard"
                elif medium_button_rect.collidepoint(event.pos):
                    state="medium"
                elif easy_button_rect.collidepoint(event.pos):
                    state="easy"
                elif scoreboard_button_rect.collidepoint(event.pos):
                    state="scoreboard"
            elif state=="scoreboard":
                if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                    state="main_menu"
    screen.fill(WHITE)
    game_state(state)
    pygame.display.update()
pygame.quit()