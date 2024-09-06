import math
import pygame


def throwingTheRock(step):
    speed = 4
    distance = 8
    time = 0
    time_by_step = 1
    # distance of the rock
    Drock = 0

    for i in range(step):
        Drock += speed * time_by_step
        time += 1
        speed = speed / 2
        gap = distance - Drock
        print(f"emplacement de la pierre : {Drock} , emplacement de l'arbre {distance}")
        # print("#"*(math.floor(Drock)-1) +"R"+"#"*(math.floor(gap)-1)+"T")
    return Drock, distance


def line_maker(screen, step, imageA, imageT):
    x1 = 360
    x2 = 1160
    y = 180
    n = 0
    for i in range(step):
        Drock, distance = throwingTheRock(n)
        # convertion dees metres en pixels (1m/100pixels)
        Drock *= 100
        distance *= 100
        pygame.draw.line(screen, (0, 0, 0), (x1, y), (x2, y), 2)
        screen.blit(imageA, (Drock + x1, y))
        screen.blit(imageT, (distance + x1, y))
        message(screen, 20, f"Distance : {Drock} metres", (0, y - 25), (0, 0, 0))
        y += 50
        n += 1


# fonction pour pouvoir ecrire quelque chose sur l'ecran
def message(screen, size, message, message_rectangle, color):
    font = pygame.font.SysFont("arial", size)
    message = font.render(message, False, color)
    screen.blit(message, message_rectangle)


def main_dichotomy():

    # init
    pygame.init()
    running = True
    start = False
    step = 6
    screen = pygame.display.set_mode((1200, 600))

    # init image
    RockInit = pygame.image.load("image/Rock.jpg")
    RockImage = pygame.transform.scale(RockInit, (20, 20))
    TreeInit = pygame.image.load("image/Tree.png")
    TreeImage = pygame.transform.scale(TreeInit, (20, 20))

    # boucle for pygame
    while running:
        screen.fill((255, 255, 255))
        message(screen, 40, "Paradoxe de dichotomie", (400, 0, 0, 0), (0, 0, 0))
        message(
            screen,
            25,
            "temps par ligne : 1s , distance total : 8m (800 pixels) ,vitesse initial de la pierre : 4m/s ",
            (10, 100, 0, 0),
            (0, 0, 0),
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                start = True
        if start:
            line_maker(screen, step, RockImage, TreeImage)
        if not start:
            message(
                screen,
                25,
                "Appuyez sur n'importe quelle touche du clavier pour afficher la simulation",
                (350, 55, 0, 0),
                (0, 0, 0),
            )

        pygame.display.flip()


if __name__ == "__main__":
    main_dichotomy()
