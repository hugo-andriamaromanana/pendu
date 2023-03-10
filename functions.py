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
LIGHT_BLUE=(173,216,230)
CLEAR_BLUE=(0,191,255)
GREY=(128,128,128)
#---------------------Importing txt-----------
f = open('mots.txt', 'r')
content = f.read()
content = content.split('\n')
content = [i.lower() for i in content]
f.close()
#---------------------Importing Json-----------
with open("scoreboard.json","r") as f:
    scoreboard = json.load(f)
#---------------------Constantes---------------------
AUTHORIZED_KEYS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def sort_score_board(scoreboard):
    return dict(sorted(scoreboard.items(), key=lambda x: x[1], reverse=True))
#---------------------Variables---------------------
input_letter=''
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
game_over=False
Easy_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[0]])
Medium_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[1]])
Hard_scoreboard_data = sort_score_board(scoreboard[([i for i in scoreboard])[2]])
running=True
state="main_menu"
sub_surface = [0, 0, 200, 200]
UPDATEEGGMANANIMATION = USEREVENT+1
start = time.time()
SCORE_COEF={
    "Easy":10**2,
    "Medium":10**3,
    "Hard":10**4
}
#Here the requirements is to store the scores in a .txt
#So i made a .txt file and a function to turn it into a dict
#In my code i use the .json file
#But this code serves as the same purpose
#---------------------txt parser--------------------------
# with open('scoreboard.txt', 'r') as f:
#     scoreboard_txt = f.read()

def turn_txt_to_dict(txt):
    return json.loads(txt)

# scoreboard = turn_txt_to_dict(scoreboard_txt)
#---------------------Functions----------------------------
#Will calculate the score, according to the time spent and the difficulty
def score_calculate(points,time_score,mode):
    return int((points/time_score)*mode)
def get_3_best(dic):
    arr=[]
    for i in dic:
        arr.append(f'{i} : {dic[i]}')
    return arr[:3]
#Animations updates
def eggman_display_every_1s():
    pygame.time.set_timer(UPDATEEGGMANANIMATION, 800)
#Hangman animations in game
def parse_subsurface(x, y, width, height, lives):
    SQUARE_SIZE = 200
    return [x + SQUARE_SIZE * (lives - 1), y, width, height]
#Time appearance
def parse_time(time):
    minutes = int(time / 60)
    seconds = int(time % 60)
    return f"{minutes}m {seconds}s"
#Handling game events
def game_time(game_vars,events): 
    #win condition
    if "_" not in game_vars['word_to_guess_display']:
        game_vars['score'] += 1
        game_vars=reset_game_vars(game_vars)
    for event in events:
        if event.type == KEYDOWN:
            if event.unicode in game_vars["used_keys"] or event.unicode not in AUTHORIZED_KEYS or event.unicode == "":
                continue
            if event.unicode not in game_vars['word_to_guess']:
                game_vars['used_keys'].append(event.unicode)
            if event.unicode in game_vars['word_to_guess']:
                for i in range(len(game_vars['word_to_guess'])):
                    if game_vars['word_to_guess'][i] == event.unicode:
                        game_vars['word_to_guess_display'][i] = event.unicode
            else:
                game_vars['lives'] -= 1
                game_vars['sub_surface'][0] += 200
    return game_vars
#Check loose to exit the game
def check_loose(game_vars):
    if game_vars['lives'] <= 0:
        return True
    return False
#Reset vars in game that aren't score
def reset_game_vars(game_vars):
    word_to_guess = list(random.choice(content).lower())
    game_vars['word_to_guess']= word_to_guess
    game_vars['word_to_guess_display']=['_' for i in word_to_guess]
    game_vars['used_keys']=[]
    game_vars['lives']=6
    game_vars['time']=0
    game_vars['sub_surface']=[0, 0, 200, 200]
    return game_vars