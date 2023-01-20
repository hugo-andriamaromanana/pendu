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

#---------------------Variables---------------------
score=0
errors=0
time_left=0
word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
word_to_guess_display = list('_ '*len(word_to_guess)) #word to guess as a list
easy_scoreboard=""
medium_scoreboard=""
hard_scoreboard=""
gamemode="Easy"
game_over=False
easy_scoreboard_data=scoreboard[([i for i in scoreboard])[0]]
medium_scoreboard_data=scoreboard[([i for i in scoreboard])[1]]
hard_scoreboard_data=scoreboard[([i for i in scoreboard])[2]]
name=""



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

def score_calculate(elapsed_time,errors_left):
    return int(1000*(errors_left/elapsed_time))

def guess_word_to_guess_display(letter):
    global word_to_guess
    global word_to_guess_display
    global score
    global errors
    if letter in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i]==letter:
                word_to_guess_display[i]=letter
    else:
        errors+=1

def check_if_win():
    global word_to_guess
    global word_to_guess_display
    if word_to_guess==word_to_guess_display:
        return True
    else:
        return False

def check_if_lose():
    global errors
    global MODE
    global gamemode
    if errors>=MODE[gamemode]["MAX_ERRORS"]:
        return True
    else:
        return False

def check_if_game_over():
    global game_over
    global time_left
    if check_if_win() or check_if_lose() or time_left<=0:
        game_over=True
        return True
    else:
        return False

def play_again():
    global word_to_guess
    global word_to_guess_display
    global score
    global errors
    global time_left
    global game_over
    global gamemode
    word_to_guess = list((random.choice(content)).lower()) #word to guess as a list
    word_to_guess_display = list('_ '*len(word_to_guess)) #word to guess as a list
    score=0
    errors=0
    time_left=0
    game_over=False
    gamemode=""#current gamemode

def set_mode(mode):
    global gamemode
    gamemode=MODE[mode]

def set_time_left():
    global gamemode
    global time_left
    time_left=MODE[gamemode]["MAX_TIME"]

def update_scoreboard():
    global gamemode
    global scoreboard
    global score
    global name
    scoreboard[gamemode][name]=score

def save_scoreboard():
    global scoreboard
    with open("scoreboard.json","w") as f:
        json.dump(scoreboard,f)

#---------------------Pygame---------------------
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

#---------------------Classes---------------------

class Button:
    def __init__(self, x, y, width, height, text, color, text_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text_surface = self.font.render(self.text, False, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width/2, self.y + self.height/2))

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
            return True
        else:
            return False

class InputBox:
    def __init__(self, x, y, width, height, text, color, text_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.font_size = font_size
        self.font = pygame.font.SysFont('Comic Sans MS', self.font_size)
        self.text_surface = self.font.render(self.text, False, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width/2, self.y + self.height/2))

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, mouse_pos):
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
            return True
        else:
            return False

    def update_text(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, False, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.width/2, self.y + self.height/2))

#---------------------Main Loop---------------------
while True:
