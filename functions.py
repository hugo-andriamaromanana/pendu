import pygame
import random
import json
from pygame.locals import *
import time
#---------------------Colors---------------------
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,165,0)
PURPLE=(128,0,128)
PINK=(255,192,203)
#---------------------Importing txt-----------
f = open('mots.txt', 'r')
content = f.read()
content = content.split('\n')
content=content[:-1]
content = [i.lower() for i in content]

#---------------------Importing Json-----------
with open("scoreboard.json","r") as f:
    scoreboard = json.load(f)

#---------------------Constantes---------------------

AUTHORIZED_KEYS = "abcdefghijklmnopqrstuvwxyz"

def sort_score_board(scoreboard):
    return dict(sorted(scoreboard.items(), key=lambda x: x[1], reverse=True))

#---------------------Variables---------------------
input_letter=''
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
game_over=False
easy_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[0]])
medium_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[1]])
hard_scoreboard_data = sort_score_board(scoreboard[([i for i in scoreboard])[2]])
running=True
state="main_menu"
sub_surface = [0, 0, 200, 200]
UPDATEEGGMANANIMATION = USEREVENT+1
confetti_list=[]
start = time.time()

#---------------------Functions----------------------------
def score_calculate(elapsed_time,errors_left):
    return int(1000*(errors_left/elapsed_time))

def get_3_best(dic):
    arr=[]
    for i in dic:
        arr.append(f'{i} : {dic[i]}')
    return arr[:3]

def eggman_display_every_1s():
    pygame.time.set_timer(UPDATEEGGMANANIMATION, 1000)

def confetti_time():
    for i in range(50):
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        width = random.randint(5, 20)
        height = random.randint(5, 20)
        confetti_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        confetti_list.append([pygame.Rect(x, y, width, height), confetti_color])

def parse_subsurface(x, y, width, height, lives):
    SQAUARE_SIZE = 200
    return [x + SQAUARE_SIZE * (lives - 1), y, width, height]

def parse_time(time):
    minutes = int(time / 60)
    seconds = int(time % 60)
    return f"{minutes}m {seconds}s"

def game_time(game_vars): 
    global score
    #win condition
    if "_" not in game_vars['word_to_guess_display']:
        print('bruh')
        game_vars['score'] += 1
        game_vars=reset_game_vars(game_vars)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.unicode in game_vars["used_keys"] or event.unicode not in AUTHORIZED_KEYS or event.unicode == "":
                continue
            if event.unicode not in game_vars['word_to_guess']:
                game_vars['used_keys'].append(event.unicode)
            print(game_vars["used_keys"])
            if event.unicode in game_vars['word_to_guess']:
                for i in range(len(game_vars['word_to_guess'])):
                    if game_vars['word_to_guess'][i] == event.unicode:
                        game_vars['word_to_guess_display'][i] = event.unicode
            else:
                game_vars['lives'] -= 1
                game_vars['sub_surface'][0] += 200
    return game_vars

def check_loose(game_vars):
    if game_vars['lives'] <= 0:
        return True
    return False

def reset_game_vars(game_vars):
    word_to_guess = list(random.choice(content).lower())
    game_vars['word_to_guess']= word_to_guess
    game_vars['word_to_guess_display']=['_' for i in word_to_guess]
    game_vars['used_keys']=[]
    game_vars['lives']=6
    game_vars['time']=0
    game_vars['sub_surface']=[0, 0, 200, 200]
    return game_vars