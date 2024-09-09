import math 
import pygame
import time

def shoot(step):
    Distance=800
    DArrow = 0
    speed = 200
    time=0
    time_by_step = 1
    LastDArrow= 0
    for i in range(step):
        # print("#" * math.floor(DArrow) + "F" + "#"*((math.floor(Distance)-math.floor(DArrow))-1) + "C")
        DArrow += speed * time_by_step
        time+=1
        # print(f"temps : {time}s , emplacement fleche : {DArrow} , cible : {Distance}")
        
        if DArrow == LastDArrow:
            break
            
        LastDArrow = DArrow
    
    return DArrow

def blit_arrow(screen,step,imageArrow):
    y = 300
    n=0
    while n<step:
        for i in range(step):
            n+=1
            Darrow = shoot(n)
            screen.blit(imageArrow, (Darrow , y))
        time.sleep(1)

        
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
    TargetInit = pygame.image.load("image/Biche.jpg")
    TargetImage = pygame.transform.scale(TargetInit, (90,150))
    ArrowInit = pygame.image.load("image/Arrow.png")
    ArrowImage = pygame.transform.scale(ArrowInit, (30, 150))

    # boucle for pygame
    while running:
        screen.fill((255, 255, 255))
        screen.blit(TargetImage,(1000,350))
        message(
            screen, 40, "Paradoxe d'Achille et la Tortue", (400, 0, 0, 0), (0, 0, 0)
        )
        message(
            screen,
            25,
            "time par ligne : 1s , distance total : 1120 pixels ,vitesse initial d'Achille et de la Tortue' : 1000 et 500 pixels",
            (10, 100, 0, 0),
            (0, 0, 0),
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        blit_arrow(screen ,step , ArrowImage)

        pygame.display.flip()


if __name__ == "__main__":
    main_arrow()
    # run_achille_tortue(20)

