import pygame
from pygame.locals import *
from functions import *
import random
#---------------------PYGAME---------------------
pygame.init()
pygame.font.init()
pygame.display.set_caption("Hangman")
screen = pygame.display.set_mode((1500, 600))
screen.fill(WHITE)
#---------------------CONST---------------------
COMIC_SANS= pygame.font.SysFont('Comic Sans MS', 30)
DISPLAYSURF = pygame.display.set_mode((800, 400))
#---------------------VARS---------------------
events = []
new_word=''
typed_word = ['_'] * 9
count_for_end_message=0
levels = ["Easy", "Medium", "Hard"]
positions = ["1st", "2nd", "3rd"]
input_name=['_ '*6]
time_spent=0
count = 1
add_word_temp=''
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
    10: "You are done. Fired",
    420: "",
    99:"Add a new word, and press ENTER to add it to the .txt",
    69:"Please, Enter a username and press ENTER",
    80:"A new word has been added to the .txt",
}
text_input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = BLACK
color_active = RED
color = color_inactive
toggle_add=False
user_set=False
active = False
visual_text=['_']*6
text_input_output = ''
def_user=''
#---------------------GUI---------------------------
#Hard button
Hard_button_rect = pygame.Rect(650, 100, 200, 50)
Hard_button_text = COMIC_SANS.render("Hard", True, BLACK)
Hard_button_rect_center=Hard_button_text.get_rect(center=Hard_button_rect.center)
#Add new word button
add_new_word_button_rect = pygame.Rect(650, 30, 300, 50)
add_new_word_button_text = COMIC_SANS.render("Add new word", True, WHITE)
add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
#Medium button
Medium_button_rect = pygame.Rect(650, 200, 200, 50)
Medium_button_text = COMIC_SANS.render("Medium", True, BLACK)
Medium_button_rect_center=Medium_button_text.get_rect(center=Medium_button_rect.center)
#Easy button
Easy_button_rect = pygame.Rect(650, 300, 200, 50)
Easy_button_text = COMIC_SANS.render("Easy", True, BLACK)
Easy_button_rect_center=Easy_button_text.get_rect(center=Easy_button_rect.center)
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
#Easy button exit
Easy_button_exit_rect = pygame.Rect(650, 500, 200, 50)
Easy_button_exit_text = COMIC_SANS.render("X", True, WHITE)
Easy_button_exit_rect_center=Easy_button_exit_text.get_rect(center=Easy_button_exit_rect.center)
#Title better luck next time
title_better_luck_next_time_rect = pygame.Rect(50, 590, 900, 50)
title_better_luck_next_time_text = COMIC_SANS.render(end_messages[count_for_end_message], True, BLACK)
title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
#Input_box_text
txt_surface= COMIC_SANS.render(text_input_output, BLACK, BLACK)
text_input_center=txt_surface.get_rect(center=text_input_box.center)
#Input name Box
input_name_box_rect = pygame.Rect(10, 100, 550, 50)
input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(input_name)), True, BLACK)
input_name_box_rect_center=input_name_box_text.get_rect(center=input_name_box_rect.center)
#------------Game_window-------------------
def game_state(state):
    global new_word
    global typed_word
    global input_name
    global game_vars
    global count_for_end_message
    #---------------------GUI---------------------------
    #--------------------Main menu-----------------------
    if state=="main_menu":
        pygame.draw.rect(screen, CLEAR_BLUE, add_new_word_button_rect)
        screen.blit(add_new_word_button_text, add_new_word_button_rect_center)
        pygame.draw.rect(screen, PINK, title_better_luck_next_time_rect)
        screen.blit(title_better_luck_next_time_text, title_better_luck_next_time_rect_center)
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(sub_surface),(200, 250))
        pygame.draw.rect(screen, BLACK, exit_button_rect)
        screen.blit(exit_button_text, exit_button_rect_center)
        pygame.draw.rect(screen, RED, Hard_button_rect)
        screen.blit(Hard_button_text, Hard_button_rect_center)
        pygame.draw.rect(screen, ORANGE, Medium_button_rect)
        screen.blit(Medium_button_text, Medium_button_rect_center)
        pygame.draw.rect(screen, YELLOW, Easy_button_rect)
        screen.blit(Easy_button_text, Easy_button_rect_center)
        pygame.draw.rect(screen, BLUE, scoreboard_button_rect)
        screen.blit(scoreboard_button_text, scoreboard_button_rect_center)
        pygame.draw.rect(screen, GREEN, title_text_rect)
        screen.blit(title_text, title_text_rect)
        pygame.draw.rect(screen, PURPLE, click_me_button_rect)
        screen.blit(click_me_button_text, click_me_button_rect_center)
        pygame.draw.rect(screen, WHITE, input_name_box_rect)
        screen.blit(input_name_box_text, input_name_box_rect_center)
    #--------------------Scoreboard-----------------------------------
    elif state=="scoreboard":
        pygame.draw.rect(scoreboard_popup, RED, scoreboard_popup_exit_button_rect)
        scoreboard_popup.blit(scoreboard_popup_exit_button_text, scoreboard_popup_exit_button_rect_center)
        scoreboard_popup.blit(COMIC_SANS.render("SCOREBOARD", True, BLUE), (400, 10))
        scoreboard_popup.blit(COMIC_SANS.render("Easy", True, YELLOW), (100, 100))
        scoreboard_popup.blit(COMIC_SANS.render("Medium", True, ORANGE), (450, 100))
        scoreboard_popup.blit(COMIC_SANS.render("Hard", True, RED), (800, 100))
    #Shows the top 3 players in the scoreboard
        for i, level in enumerate(levels):
            scoreboard_data = eval(f"{level}_scoreboard_data")
            x = 20 + 350 * i
            for j, position in enumerate(positions):
                y = 200 + 100 * j
                text = f"{position} {get_3_best(scoreboard_data)[j]}"
                scoreboard_popup.blit(COMIC_SANS.render(text, True, BLACK), (x, y))
    #---------------------Hard level---------------------------------------
    elif state=="Hard":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Hard", True, RED), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars,events)
    #--------------------Medium lvl-------------------------------
    elif state=="Medium":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Medium", True, ORANGE), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars,events)
    #------------------Easy lvl--------------------------------
    elif state=="Easy":
        DISPLAYSURF.blit(pygame.image.load("hangman.png").subsurface(game_vars["sub_surface"]),(200, 250))
        DISPLAYSURF.blit(COMIC_SANS.render("Difficulty = Easy", True, YELLOW), (400, 10))
        DISPLAYSURF.blit(COMIC_SANS.render("Guess the word!", True, GREEN), (400, 100))
        DISPLAYSURF.blit(COMIC_SANS.render(' '.join(game_vars['word_to_guess_display']), True, BLACK), (500, 400))
        DISPLAYSURF.blit(COMIC_SANS.render("Guesses left: "+str(game_vars['lives']), True, BLACK), (100, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Time : " + parse_time(time.time() - start), True, (0, 0, 0)), (500, 500))
        DISPLAYSURF.blit(COMIC_SANS.render("Letters used: "+", ".join(game_vars['used_keys']), True, BLACK), (100, 600))
        DISPLAYSURF.blit(COMIC_SANS.render("Score: "+str(game_vars['score']), True, BLACK), (500, 600))
        game_vars = game_time(game_vars,events)

#Animations
eggman_display_every_1s()
#---------------------------Main logic------------------------------------
while running:
    #--------------------Logic behind the toggle add new word button----------------
    if toggle_add == False:
        add_new_word_button_text = COMIC_SANS.render("Add new word", True, WHITE)
        add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
    #--------------------Custom messages for lost games------------------------------
    if count_for_end_message not in [i for i in end_messages]:
        count_for_end_message=0
    #-------------------Logic behind end of the game / WIN CONDITIONS------------------------------------
    if check_loose(game_vars):
        #----------------Add to scoreboard if score higher than top 3-------------------
        if int(score_calculate(game_vars['score'],int(time.time()-start),SCORE_COEF[state])) > int(Hard_scoreboard_data[[i for i in Hard_scoreboard_data][2]]):
            scoreboard[state][def_user]=int(score_calculate(game_vars['score'],int(time.time()-start),SCORE_COEF[state]))
            with open('scoreboard.json','w') as f:
                json.dump(scoreboard,f,indent=4)
            count_for_end_message=420
            end_messages[count_for_end_message]=f'Congrats, check the {state} leaderboard!'
            game_vars['score']=0
            state="main_menu"
        #-----------------Quit if too much testing------------------------------
        if count_for_end_message==11:
            running=False
        title_better_luck_next_time_text = COMIC_SANS.render(end_messages[count_for_end_message], True, BLACK)
        title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
        game_vars=reset_game_vars(game_vars)
        state="main_menu"
    #--------------------Handling events-------------------------------------------
    events = pygame.event.get()
    for event in events:
        #------------------Return Keys-----------------------------
        if event.type == pygame.QUIT:
            running = False
        #--------------------Logic Buttons---------------------------
        if event.type == pygame.MOUSEBUTTONDOWN:
            #-----------------Main menu logic---------------------
            if state=="main_menu":
                #Add new word button
                if add_new_word_button_rect.collidepoint(event.pos):
                    title_better_luck_next_time_text = COMIC_SANS.render(end_messages[99], True, BLACK)
                    title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                    active=False
                    toggle_add=True
                    add_new_word_button_text = COMIC_SANS.render(' '.join(typed_word), True, WHITE)
                    add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
                #Custom messages display
                if click_me_button_rect.collidepoint(event.pos):
                    title_better_luck_next_time_text = COMIC_SANS.render(end_messages[random.choice([i for i in range(10)])], True, BLACK)
                    title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                #Input name button
                if input_name_box_rect.collidepoint(event.pos):
                    toggle_add=False
                    active = not active
                    input_name=['_']*6
                    input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(input_name)), True, BLACK)
                    text_input_output=''
                    visual_text=['_']*6
                    def_user=''
                else:
                    active = False
                color = color_active if active else color_inactive
                #Exit button
                if exit_button_rect.collidepoint(event.pos):
                    running=False
                #Hard button
                elif Hard_button_rect.collidepoint(event.pos):
                    reset_game_vars(game_vars)
                    #If no user name, lvls can't be accesssed
                    if def_user=='':
                        title_better_luck_next_time_text = COMIC_SANS.render(end_messages[69], True, BLACK)
                        title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                        continue
                    #Show different message if death
                    if def_user!='': 
                        count_for_end_message+=1
                    state="Hard"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif Medium_button_rect.collidepoint(event.pos):
                    reset_game_vars(game_vars)
                    if def_user=='':
                        title_better_luck_next_time_text = COMIC_SANS.render(end_messages[69], True, BLACK)
                        title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                        continue
                    if def_user!='': 
                        count_for_end_message+=1
                    state="Medium"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                elif Easy_button_rect.collidepoint(event.pos):
                    reset_game_vars(game_vars)
                    if def_user=='':
                        title_better_luck_next_time_text = COMIC_SANS.render(end_messages[69], True, BLACK)
                        title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                        continue
                    state="Easy"
                    start=time.time()
                    game_vars["word_to_guess"] = random.choice(content)
                    game_vars["word_to_guess_display"] = ["_"] * len(game_vars["word_to_guess"])
                #Updates scoreboards when scoreboard button is pressed
                elif scoreboard_button_rect.collidepoint(event.pos):
                    Easy_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[0]])
                    Medium_scoreboard_data=sort_score_board(scoreboard[([i for i in scoreboard])[1]])
                    Hard_scoreboard_data = sort_score_board(scoreboard[([i for i in scoreboard])[2]])
                    state="scoreboard"
            #exit button for scoreboard
            elif state=="scoreboard":
                if scoreboard_popup_exit_button_rect.collidepoint(event.pos):
                    state="main_menu"
        #Handling typing events
        if event.type == pygame.KEYDOWN:
            #logic behind Add new word button
            if toggle_add:
                if event.unicode == '\x08':
                    add_word_temp=add_word_temp[:-1]
                    typed_word=[i for i in add_word_temp]+['_']*(len(typed_word)-len(add_word_temp))
                    add_new_word_button_text = COMIC_SANS.render(' '.join(typed_word), True, WHITE)
                    add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    continue
                if event.unicode in AUTHORIZED_KEYS:
                    add_word_temp+=event.unicode
                    typed_word=[i for i in add_word_temp]+['_']*(len(typed_word)-len(add_word_temp))
                    add_new_word_button_text = COMIC_SANS.render(' '.join(typed_word), True, WHITE)
                    add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
                if event.key == pygame.K_RETURN:
                    content.append(add_word_temp.lower())
                    f= open("mots.txt","w")
                    f.write('\n'.join(content))
                    f.close()
                    add_word_temp=''
                    typed_word=['_']*6
                    add_new_word_button_text = COMIC_SANS.render("Add new word", True, WHITE)
                    add_new_word_button_rect_center=add_new_word_button_text.get_rect(center=add_new_word_button_rect.center)
                    title_better_luck_next_time_text = COMIC_SANS.render(end_messages[80], True, BLACK)
                    title_better_luck_next_time_rect_center=title_better_luck_next_time_text.get_rect(center=title_better_luck_next_time_rect.center)
                    toggle_add=False
            #Logic behind username button
            if active:
                input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(visual_text)), True, BLACK)
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    continue
                input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(visual_text)), True, BLACK)
                if len(text_input_output) < 6:
                    visual_text[len(text_input_output)]=event.unicode
                if len(text_input_output) >6:
                    text_input_output=text_input_output[:-1]
                input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(visual_text)), True, BLACK)
                if event.key == pygame.K_RETURN:
                    user_set=True
                    input_name=text_input_output[:6]
                    active = not active
                    def_user=input_name
                    input_name_box_text = pygame.font.SysFont('Comic Sans MS', 30).render(('Welcome to Hangman '+''.join(def_user))+'!', True, BLACK)
                elif event.key == pygame.K_BACKSPACE:
                    visual_text=list((''.join(visual_text)).replace('\x08','_'))
                    visual_text[len(text_input_output)-1]='_'
                    input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(visual_text)), True, BLACK)
                    text_input_output = text_input_output[:-1]
                else:
                    text_input_output += event.unicode
            if event.key == pygame.K_ESCAPE:
                state="main_menu"
        #Animations
        if event.type == UPDATEEGGMANANIMATION and state=="main_menu":
            if not active:
                if text_input_output == '':
                    if (count % 2 == 0):
                        input_name_box_text = COMIC_SANS.render('Please enter your name: '+(' '.join(input_name)), True, BLACK)
                    else:
                        input_name_box_text = COMIC_SANS.render('Please enter your name: ', True, BLACK)
                    count += 1
            sub_surface[0]+=200
            if sub_surface[0]>1201: 
                sub_surface[0]=0
        #Exit
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    game_state(state)
    pygame.display.update()
pygame.quit()