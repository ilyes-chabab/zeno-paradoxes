import pygame
from dichotomy import paradoxDichotomy
pygame.init()

initialDistance = 240.0
tolerance = 0.000240

def addingRocks():
    for i in p:
        surf.blit(newRock, (i,250))

surf = pygame.display.set_mode((800,600))
surf.fill((255,255,255)) # Setting background color on white
tree = pygame.image.load("pictures/arbre-removebg-preview.png").convert_alpha()
newTree = pygame.transform.scale(tree, (350,300))
rock = pygame.image.load("pictures/pierre-qui-roule.png").convert_alpha()
newRock = pygame.transform.scale(rock, (150,100))
run =  True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        surf.blit(newTree, (500,150))
        p = paradoxDichotomy(initialDistance,tolerance, mode='GUI')
        initialPosition = 20
        surf.blit(newRock, (initialPosition,250))
        for i in p:
            surf.blit(newRock, (initialPosition+i,250))
        pygame.display.flip()
pygame.quit()


