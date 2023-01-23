import pygame
import random
import json
from pygame.locals import *
import time

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
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,165,0)
PURPLE=(128,0,128)
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
input_letter=''
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
easy_scoreboard=""
medium_scoreboard=""
hard_scoreboard=""
game_over=False
easy_scoreboard_data=scoreboard[([i for i in scoreboard])[0]]
medium_scoreboard_data=scoreboard[([i for i in scoreboard])[1]]
hard_scoreboard_data=scoreboard[([i for i in scoreboard])[2]]
running=True
state="main_menu"
sub_surface = [0, 0, 200, 200]
UPDATEEGGMANANIMATION = USEREVENT+1
confetti_list=[]
start = time.time()
used_keys=[]
score=0
lives = 6
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
    word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
    word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
    score=0
    errors=0
    time_left=0
    game_over=False

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

# def game_time():
#     global lives
#     global used_keys
#     global sub_surface
#     global score
#     global word_to_guess_display
#     global word_to_guess
#     while lives > 0:
#         if "_" not in word_to_guess_display:
#             score += 1 
#             used_keys = []
#             sub_surface = [0, 0, 200, 200]
#         for event in pygame.event.get():
#             if event.type == KEYDOWN:
#                 if event.unicode in used_keys or event.unicode not in AUTHORIZED_KEYS or event.unicode == "":
#                     continue
#             used_keys.append(event.unicode)
#             if event.unicode in word_to_guess:
#                 for i in range(len(word_to_guess)):
#                     if word_to_guess[i] == event.unicode:
#                         word_to_guess_display[i] = event.unicode
#             else:
#                 lives -= 1
#                 sub_surface[0] += 200