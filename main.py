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
