import pygame

pygame.init()

# Create the main window
screen = pygame.display.set_mode((800, 600))

# Create a button
button = pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 50))

# Add text to the button
font = pygame.font.Font(None, 30)
text = font.render("Click me", True, (255, 255, 255))
text_rect = text.get_rect(center=(75, 75))
screen.blit(text, text_rect)
pygame.display.update()

# Create the pop-up window
popup = pygame.display.set_mode((400, 300))
popup.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            # Check if the button was clicked
            if button.collidepoint(pos):
                # Draw elements on the pop-up window
                pygame.draw.rect(popup, (255, 0, 0), (50, 50, 100, 50))
                text = font.render("OK", True, (255, 255, 255))
                text_rect = text.get_rect(center=(200, 150))
                popup.blit(text, text_rect)
                pygame.display.update()
                # Wait for the user to close the pop-up window
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

