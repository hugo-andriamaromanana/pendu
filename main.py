import pygame
from pygame.locals import *
from functions import *
import random

#---------------------Pygame---------------------
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1500, 600))
screen.fill(WHITE)

#---------------------Main Menu---------------------

COMIC_SANS= pygame.font.SysFont('Comic Sans MS', 30)
DISPLAYSURF = pygame.display.set_mode((800, 400))

game_vars = {
    "lives": 6,
    "used_keys": [],
    "sub_surface" : [0,0,200,200],
    "word_to_guess" : random.choice(content),
    "word_to_guess_display":["_"] * len(random.choice(content)),
    "score":0
}

#Hard button
hard_button_rect = pygame.Rect(650, 100, 200, 50)
hard_button_text = COMIC_SANS.render("Hard", True, BLACK)
hard_button_rect_center=hard_button_text.get_rect(center=hard_button_rect.center)
#Medium button
medium_button_rect = pygame.Rect(650, 200, 200, 50)
medium_button_text = COMIC_SANS.render("Medium", True, BLACK)
medium_button_rect_center=medium_button_text.get_rect(center=medium_button_rect.center)
#Easy button
easy_button_rect = pygame.Rect(650, 300, 200, 50)
easy_button_text = COMIC_SANS.render("Easy", True, BLACK)
easy_button_rect_center=easy_button_text.get_rect(center=easy_button_rect.center)
#Exit button
exit_button_rect = pygame.Rect(650, 500, 200, 50)
exit_button_text = COMIC_SANS.render("Exit", True, WHITE)
exit_button_rect_center=exit_button_text.get_rect(center=exit_button_rect.center)
#Scoreboard button
scoreboard_button_rect = pygame.Rect(650, 400, 200, 50)
scoreboard_button_text = COMIC_SANS.render("Scoreboard", True, WHITE)
scoreboard_button_rect_center=scoreboard_button_text.get_rect(center=scoreboard_button_rect.center)
#Scoreboard popup window
scoreboard_popup=pygame.display.set_mode((1000, 650))
scoreboard_popup.fill(WHITE)
#Scoreboard popup window exit button
scoreboard_popup_exit_button_rect = pygame.Rect(700,10, 50, 50)
scoreboard_popup_exit_button_text = COMIC_SANS.render("X", True, WHITE)
scoreboard_popup_exit_button_rect_center=scoreboard_popup_exit_button_text.get_rect(center=scoreboard_popup_exit_button_rect.center)
#Title text
title_text = COMIC_SANS.render("Hangman: now on Windows XP!", True, BLACK)
title_text_rect=title_text.get_rect(center=(400, 50))
#Click Me! button
click_me_button_rect = pygame.Rect(300, 500, 200, 50)
click_me_button_text = COMIC_SANS.render("Click Me!", True, WHITE)
click_me_button_rect_center=click_me_button_text.get_rect(center=click_me_button_rect.center)


#------------Game_window-------------------
def game_state(state):
    global game_vars
    if state=="main_menu":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(sub_surface),(200, 250))
        pygame.draw.rect(screen, BLACK, exit_button_rect)
        screen.blit(exit_button_text, exit_button_rect_center)
        pygame.draw.rect(screen, RED, hard_button_rect)
        screen.blit(hard_button_text, hard_button_rect_center)
        pygame.draw.rect(screen, ORANGE, medium_button_rect)
        screen.blit(medium_button_text, medium_button_rect_center)
        pygame.draw.rect(screen, YELLOW, easy_button_rect)
        screen.blit(easy_button_text, easy_button_rect_center)
        pygame.draw.rect(screen, BLUE, scoreboard_button_rect)
        screen.blit(scoreboard_button_text, scoreboard_button_rect_center)
        pygame.draw.rect(screen, GREEN, title_text_rect)
        screen.blit(title_text, title_text_rect)
        pygame.draw.rect(screen, PURPLE, click_me_button_rect)
        screen.blit(click_me_button_text, click_me_button_rect_center)
    elif state=="scoreboard":
        pygame.draw.rect(scoreboard_popup, RED, scoreboard_popup_exit_button_rect)
        scoreboard_popup.blit(scoreboard_popup_exit_button_text, scoreboard_popup_exit_button_rect_center)
        scoreboard_popup.blit(COMIC_SANS.render("SCOREBOARD", True, BLUE), (400, 10))
        scoreboard_popup.blit(COMIC_SANS.render("Easy", True, YELLOW), (100, 100))
        scoreboard_popup.blit(COMIC_SANS.render("Medium", True, ORANGE), (450, 100))
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
    elif state=="hard":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = HARD", True, RED), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars)
    elif state=="medium":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Medium", True, ORANGE), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(score), True, BLACK), (500, 600))
        game_vars = game_time(game_vars)
    elif state=="easy":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Easy", True, YELLOW), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(score), True, BLACK), (500, 600))
        game_vars = game_time(game_vars)

eggman_display_every_1s()
while running:
    if check_loose(game_vars):
        game_vars=reset_game_vars(game_vars)
        state="main_menu"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state=="main_menu":
                if click_me_button_rect.collidepoint(event.pos):
                    screen.fill((255, 255, 255))
                    confetti_time()
                    for confetti in confetti_list:
                        confetti[0].y += 1
                    for confetti in confetti_list:
                        pygame.draw.rect(screen, confetti[1], confetti[0])
                if exit_button_rect.collidepoint(event.pos):
                    running=False
                elif hard_button_rect.collidepoint(event.pos):
                    state="hard"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif medium_button_rect.collidepoint(event.pos):
                    state="medium"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif easy_button_rect.collidepoint(event.pos):
                    state="easy"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif lives==0:
                    message = COMIC_SANS.render("Out of lives! Maybe try something easier?", True, (255, 255, 255))
                elif scoreboard_button_rect.collidepoint(event.pos):
                    state="scoreboard"
            elif state=="scoreboard":
                if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                    state="main_menu"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                state="main_menu"
        if event.type == UPDATEEGGMANANIMATION and state=="main_menu":
            sub_surface[0]+=200
            if sub_surface[0]>1201: 
                sub_surface[0]=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    game_state(state)
    pygame.display.update()
pygame.quit()