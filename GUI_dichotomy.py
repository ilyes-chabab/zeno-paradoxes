import pygame
from dichotomy2 import paradoxDichotomy

def main_dichotomy():
    pygame.init()

    initialDistance = 800
    tolerance = 0.000240


    surf = pygame.display.set_mode((800, 600))
    surf.fill((255, 255, 255))  # Setting background color on white
    tree = pygame.image.load("pictures/arbre-removebg-preview.png").convert_alpha()
    newTree = pygame.transform.scale(tree, (350, 300))
    rock = pygame.image.load("pictures/cercle.png").convert_alpha()
    newRock = pygame.transform.scale(rock, (150, 100))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            surf.blit(newTree, (500, 150))
            l = paradoxDichotomy(initialDistance, tolerance)
            initialPosition = 600
            surf.blit(newRock, (initialPosition, 250))
            for i in l:
                surf.blit(newRock, (initialPosition - i,250))
            pygame.display.flip()
    pygame.quit()
