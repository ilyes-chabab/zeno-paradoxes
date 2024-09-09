import pygame
from Achille_CLI import main_achille_et_la_tortue
from GUI_dichotomy import main_dichotomy
from Arrow_GUI import main_arrow


# func to write on the screen with pygame
def message(screen, size, message, message_rectangle, color):
    font = pygame.font.SysFont("arial", size)
    message = font.render(message, False, color)
    screen.blit(message, message_rectangle)


def main_pygame():

    # init
    pygame.init()
    running = True
    screen = pygame.display.set_mode((1200, 600))
    police = pygame.font.SysFont("arial", 30)

    AchilleEtLaTortueButton = pygame.draw.rect(screen, (0, 0, 0), (50, 200, 300, 100))
    AchilleEtLaTortueText = police.render("Achille et la tortue", 1, (0, 0, 0))

    DichotomyButton = pygame.draw.rect(screen, (0, 0, 0), (400, 200, 300, 100))
    DichotomyText = police.render("Dichotomy", 1, (0, 0, 0))

    ArrowButton = pygame.draw.rect(screen,(0, 0, 0), (750, 200, 300, 100))
    ArrowText = police.render("Arrow", 1, (0, 0, 0))

    

    # boucle for pygame
    while running:
        screen.fill((255, 255, 255))


        pygame.draw.rect(screen, (255, 0, 0), (50, 200, 300, 100))
        screen.blit(AchilleEtLaTortueText, (60, 250))

        pygame.draw.rect(screen, (255, 0, 0), (400, 200, 300, 100))
        screen.blit(DichotomyText, (400, 250))

        pygame.draw.rect(screen, (255, 0, 0), (750, 200, 300, 100))
        screen.blit(ArrowText, (750, 250))


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AchilleEtLaTortueButton.collidepoint(event.pos):
                    main_achille_et_la_tortue()
                
                elif DichotomyButton.collidepoint(event.pos):
                    main_dichotomy()
                
                elif ArrowButton.collidepoint(event.pos):
                    main_arrow()

        pygame.display.flip()


if __name__ == "__main__":
    main_pygame()
