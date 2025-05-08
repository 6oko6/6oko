import pygame
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("6oko Menu")
clock = pygame.time.Clock()

# Couleurs et police
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont("Courier New", 60, bold=True)

# Texte/logo
text = "6oko"
text_surface = font.render(text, True, WHITE)
text_rect = text_surface.get_rect()
text_rect.topleft = (100, 100)

# Vitesse du logo
velocity = [3, 3]  # [x_speed, y_speed]

def draw_logo():
    global text_surface, text_rect, velocity

    # Bouger le logo
    text_rect.x += velocity[0]
    text_rect.y += velocity[1]

    # Rebonds sur les bords
    if text_rect.right >= WIDTH or text_rect.left <= 0:
        velocity[0] = -velocity[0]
    if text_rect.bottom >= HEIGHT or text_rect.top <= 0:
        velocity[1] = -velocity[1]

    # Dessiner le texte
    screen.blit(text_surface, text_rect)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_logo()
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
