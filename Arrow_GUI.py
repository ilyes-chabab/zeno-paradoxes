import math
import pygame
import time


def shoot(step):
    Distance = 800
    DArrow = 0
    speed = 200
    time = 0
    time_by_step = 1
    LastDArrow = 0
    gap = 0
    for i in range(step):
        # print("#" * math.floor(DArrow) + "F" + "#"*((math.floor(Distance)-math.floor(DArrow))-1) + "C")
        DArrow += speed * time_by_step
        gap = Distance - DArrow
        time += 1
        # print(f"temps : {time}s , emplacement fleche : {DArrow} , cible : {Distance}")

        if DArrow == LastDArrow:
            break

        LastDArrow = DArrow

    return DArrow, gap


def blit_arrow(screen, step, imageArrow, imageTarget):
    y_arrow = 150
    y_biche = 100
    n = 0
    for i in range(step):
        n += 1
        Darrow, gap = shoot(n)
        screen.blit(imageTarget, (950, y_biche))
        screen.blit(imageArrow, (Darrow, y_arrow))
        message(screen, 20, f"gap : {gap} pixels", (0, y_arrow - 25), (0, 0, 0))
        y_arrow += 120
        y_biche += 120


# func to write on the screen
def message(screen, size, message, message_rectangle, color):
    font = pygame.font.SysFont("arial", size)
    message = font.render(message, False, color)
    screen.blit(message, message_rectangle)


def main_arrow():

    # init
    pygame.init()
    running = True
    step = 4
    screen = pygame.display.set_mode((1200, 600))

    # init image
    TargetInit = pygame.image.load("image/Biche.jpeg")
    TargetImage = pygame.transform.scale(TargetInit, (90, 110))
    ArrowInit = pygame.image.load("image/Arrow.png")
    ArrowImage = pygame.transform.scale(ArrowInit, (150, 30))

    # boucle for pygame
    while running:
        screen.fill((255, 255, 255))
        message(screen, 40, "Paradoxe de la fleche", (400, 0, 0, 0), (0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        blit_arrow(screen, step, ArrowImage, TargetImage)

        pygame.display.flip()


if __name__ == "__main__":
    main_arrow()
    # run_achille_tortue(20)
