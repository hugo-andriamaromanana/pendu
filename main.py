#Hangman using Pygame only using 6 letter words

import pygame
import random
import time
import json
#---------------------Setup---------------------

#---------------------Importing Files-----------

#---------------------Importing txt-----------
#open the file
f = open('mots.txt', 'r')
#read the file
content = f.read()
#Make the file a list
content = content.split('\n')
#remove tag
content=content[1:]
#make all the words lowercase
content = [i.lower() for i in content]

#---------------------Importing Json-----------

with open("scoreboard.json","r") as f:
    scoreboard = json.load(f)


#---------------------Constantes---------------------
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

#---------------------Variables---------------------
score=0
errors=0
time_left=0
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_'*len(word_to_guess)) #word to guess as a list
easy_scoreboard=""
medium_scoreboard=""
hard_scoreboard=""
easy_scoreboard_data=scoreboard[([i for i in scoreboard])[0]]
medium_scoreboard_data=scoreboard[([i for i in scoreboard])[1]]
hard_scoreboard_data=scoreboard[([i for i in scoreboard])[2]]


#---------------------Functions----------------------------

def sort_scoreboard_data_by_score():
    global easy_scoreboard_data
    global medium_scoreboard_data
    global hard_scoreboard_data
    easy_scoreboard_data=dict(sorted(easy_scoreboard_data.items(), key=lambda x: x[1], reverse=True))
    medium_scoreboard_data=dict(sorted(medium_scoreboard_data.items(), key=lambda x: x[1], reverse=True))
    hard_scoreboard_data=dict(sorted(hard_scoreboard_data.items(), key=lambda x: x[1], reverse=True))

def scoreboardprint_sorted():
    global easy_scoreboard
    global medium_scoreboard
    global hard_scoreboard
    for i in easy_scoreboard_data:
        easy_scoreboard+=i+" : "+str(easy_scoreboard_data[i])+" points"+"\n"
    for i in medium_scoreboard_data:
        medium_scoreboard+=i+" : "+str(medium_scoreboard_data[i])+" points"+"\n"
    for i in hard_scoreboard_data:
        hard_scoreboard+=i+" : "+str(hard_scoreboard_data[i])+" points"+"\n"

sort_scoreboard_data_by_score()
scoreboardprint_sorted()
print(easy_scoreboard)

def score_calculate(elapsed_time,tries_left):
    return int(1000*(tries_left/elapsed_time))

