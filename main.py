import pygame
from pygame.locals import *
from functions import *
import random

#---------------------Pygame---------------------
pygame.init()
pygame.font.init()
pygame.mixer.init()
# pygame.mixer.music.load("DOKI.mp3")
# pygame.mixer.music.play(-1)
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1500, 600))
screen.fill(WHITE)

#---------------------Main Menu---------------------
COMIC_SANS= pygame.font.SysFont('Comic Sans MS', 30)
DISPLAYSURF = pygame.display.set_mode((800, 400))
count_for_end_message=0
input_name=['_ '*6]
time_spent=0
count = 1
game_vars = {
    "lives": 6,
    "used_keys": [],
    "sub_surface" : [0,0,200,200],
    "word_to_guess" : random.choice(content),
    "word_to_guess_display":["_"] * len(random.choice(content)),
    "score":0
}
end_messages={
    0:"Good Luck!",
    1: "Better luck next time!",
    2: "Try something else!",
    3: "Keep on going!",
    4: "You can do better!",
    5: "I'm losing faith in you!",
    6: "You're not even trying!",
    7: "?????????????????????????",
    8: "You're a disgrace to humanity!",
    9: "Your parents wasted their time on you!",
    10: "You are done. Fired"
}
text_input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = BLACK
color_active = RED
color = color_inactive
user_set=False
active = False
temp_text=['_']*6
text_input_output = ''
#---------------------GUI--------------------------------------
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
#Input name Box
input_name_box_rect = pygame.Rect(100, 95, 200, 30)
input_name_box_text = COMIC_SANS.render((''.join(input_name)), True, BLACK)
input_name_box_rect_center=input_name_box_text.get_rect(center=input_name_box_rect.center)
#Click Me! button
click_me_button_rect = pygame.Rect(300, 500, 200, 50)
click_me_button_text = COMIC_SANS.render("Click Me!", True, WHITE)
click_me_button_rect_center=click_me_button_text.get_rect(center=click_me_button_rect.center)
#easy button exit
easy_button_exit_rect = pygame.Rect(650, 500, 200, 50)
easy_button_exit_text = COMIC_SANS.render("X", True, WHITE)
easy_button_exit_rect_center=easy_button_exit_text.get_rect(center=easy_button_exit_rect.center)
#Title better luck next time
title_better_luck_next_time_rect = pygame.Rect(50, 590, 900, 50)
title_better_luck_next_time_text = COMIC_SANS.render(end_messages[count_for_end_message], True, BLACK)
title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
#Input_box_text
txt_surface= COMIC_SANS.render(text_input_output, BLACK, BLACK)
width = max(200, txt_surface.get_rect().width+10)
text_input_box.w = width

#------------Game_window-------------------
def game_state(state):
    global game_vars
    if state=="main_menu":
        pygame.draw.rect(screen, PINK, title_better_luck_next_time_rect)
        screen.blit(title_better_luck_next_time_text, title_better_luck_next_time_rect_center)
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
        pygame.draw.rect(screen, WHITE, input_name_box_rect)
        screen.blit(input_name_box_text, input_name_box_rect_center)
        if text_input_output!=input_name:
            pygame.draw.rect(screen, color, (100, 95, 200, 40), 1)
            screen.blit(txt_surface, (text_input_box.x+5, text_input_box.y+5))


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
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars)
    elif state=="easy":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Easy", True, YELLOW), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars)

eggman_display_every_1s()
while running:
    if check_loose(game_vars):
        if int(score_calculate(game_vars['score'],int(time.time()-start),SCORE_COEF[state])) > int(hard_scoreboard_data[[i for i in hard_scoreboard_data][2]]):
            scoreboard[state]["".join(input_name)]=int(score_calculate(game_vars['score'],int(time.time()-start),SCORE_COEF[state]))
        if count_for_end_message==11:
            running=False
        count_for_end_message+=1
        title_better_luck_next_time_text = COMIC_SANS.render(end_messages[count_for_end_message], True, BLACK)
        title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
        game_vars=reset_game_vars(game_vars)
        state="main_menu"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if state=="main_menu":
                if text_input_box.collidepoint(event.pos):
                    active = not active
                    input_name=['_ '*6]
                    input_name_box_text = COMIC_SANS.render((''.join(input_name)), True, BLACK)
                else:
                    active = False
                color = color_active if active else color_inactive
                if exit_button_rect.collidepoint(event.pos):
                    running=False
                elif hard_button_rect.collidepoint(event.pos):
                    state="hard"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                    if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                        state="main_menu"
                elif medium_button_rect.collidepoint(event.pos):
                    state="medium"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                    if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                        state="main_menu"
                elif easy_button_rect.collidepoint(event.pos):
                    state="easy"
                    if easy_button_exit_rect.collidepoint(event.pos):
                        state="main_menu"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif scoreboard_button_rect.collidepoint(event.pos):
                    state="scoreboard"
            elif state=="scoreboard":
                if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                    state="main_menu"
        if event.type == pygame.KEYDOWN:
            if active:
                input_name_box_text = pygame.font.SysFont('Comic Sans MS', 30).render((' '.join(temp_text)), True, BLACK)
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    continue
                temp_text[len(text_input_output)]=event.unicode
                input_name_box_text = pygame.font.SysFont('Comic Sans MS', 30).render(' '.join(temp_text), True, BLACK)
                if event.key == pygame.K_RETURN:
                    user_set=True
                    input_name=text_input_output
                    input_name_box_text = pygame.font.SysFont('Comic Sans MS', 30).render(('Welcome to Hangman '+''.join(input_name))+'!', True, BLACK)
                    active = not active
                elif event.key == pygame.K_BACKSPACE:
                    temp_text=list((''.join(temp_text)).replace('\x08','_'))
                    temp_text[len(''.join(temp_text).replace('_',''))-1]='_'
                    input_name_box_text = pygame.font.SysFont('Comic Sans MS', 30).render(' '.join(temp_text), True, BLACK)
                    text_input_output = text_input_output[:-1]
                else:
                    text_input_output += event.unicode
            if event.key == pygame.K_ESCAPE:
                state="main_menu"
        if event.type == UPDATEEGGMANANIMATION and state=="main_menu":
            if not active:
                if text_input_output == '':
                    if (count % 2 == 0):
                        input_name=['_ '*6]
                        input_name_box_text = COMIC_SANS.render((''.join(input_name)), True, BLACK)
                    else:
                        input_name=['']
                        input_name_box_text = COMIC_SANS.render((''.join(input_name)), True, BLACK)
                    count += 1
            if count > 10:
                count=0
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