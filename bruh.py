import pygame
import random

# Initialize Pygame
pygame.init()

# Set the size of the screen (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Confetti Animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create a list to store the confetti rectangles and colors
confetti_list = []

# Create the confetti
for i in range(50):
    x = random.randint(0, 700)
    y = random.randint(0, 500)
    width = random.randint(5, 20)
    height = random.randint(5, 20)
    confetti_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    confetti_list.append([pygame.Rect(x, y, width, height), confetti_color])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Move the confetti down the screen
    for confetti in confetti_list:
        confetti[0].y += 1

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill((255, 255, 255))

    # Draw the confetti on the screen
    for confetti in confetti_list:
        pygame.draw.rect(screen, confetti[1], confetti[0])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()