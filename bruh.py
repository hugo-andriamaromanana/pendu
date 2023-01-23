import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a rectangle
rect = pygame.Rect(100, 100, 150, 50)

# Create a font object using "Comic Sans MS"
comic_sans = pygame.font.SysFont('Comic Sans MS', 30)

# Render the text
text = comic_sans.render("My Text", True, (255, 255, 255))

# Create a surface with the text
text_rect = text.get_rect(center=rect.center)

# Fill the rectangle with a color
pygame.draw.rect(screen, (255, 0, 0), rect)

# Blit the text surface to the screen
screen.blit(text, text_rect)

pygame.display.update()