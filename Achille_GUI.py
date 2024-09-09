import math
import pygame


"""
this function return the distance of achille , the turtle and the gap between them. 

argument : 
step : the number of step for the boucle ( it's the number of second while the simulation)

variable:
Da = Distance of achille 
Dt = Distance of Turtle 
gap = gap between them
time total = the total time ( in second )
time by step = the time by iteration (in second )

a boucle put Distance of achille to the distance of turtle , divide de speed of turtle by 2  ,
put distance of turtle according to his speed ( D = S * T) and add the time by step to the total time
"""


def run_achille_tortue(step):

    Da = 2
    Dt = 502
    gap = Dt - Da
    time_total = 1
    time_by_step = 1
    St = 500

    # print("#" * math.floor(Da-1) + "A" + "#"*((Dt-math.floor(Da))-1) + "T" + "#"*3)
    for i in range(step):
        Da = Dt
        St = St / 2
        Dt += St * time_by_step
        time_total += time_by_step

        # print("#" * math.floor(Da) + "A" + "#"*((math.floor(Dt)-math.floor(Da))-1) + "T" + "#"*3)
        # print("time : " ,time_total ,"distance achille : " , Da , "distance tortue", Dt)
        gap = Dt - Da
    return Da, Dt, gap


"""
function to make the lines where achille and turtle run and show their position on the line 

argument :
screen = the size of the screen for pygame
step = the number of stepfor the creation of lines
imageA = image of achille
imageT = image of turtle 

variable : 
x1 and x2: the start of the line  end the end of the line for the width
y : the height of the line 
n = the number of iteration for the step 

in each step , a line is made 50 pixels lower(y += 50) with the pos of achille and the turtle  .


"""


def line_maker(screen, step, imageA, imageT):
    x1 = 80
    x2 = 1200
    y = 180
    n = 0
    for i in range(step):
        Da, Dt, gap = run_achille_tortue(n)
        pygame.draw.line(screen, (0, 0, 0), (x1, y), (x2, y), 2)
        screen.blit(imageA, (Da + x1, y))
        screen.blit(imageT, (Dt + x1, y))
        message(screen, 20, f"gap : {gap} pixels", (0, y - 25), (0, 0, 0))
        y += 50
        n += 1


# func to write on the screen
def message(screen, size, message, message_rectangle, color):
    font = pygame.font.SysFont("arial", size)
    message = font.render(message, False, color)
    screen.blit(message, message_rectangle)


def main_achille_et_la_tortue():

    # init
    pygame.init()
    running = True
    step = 8
    screen = pygame.display.set_mode((1200, 600))

    # init image
    AchilleInit = pygame.image.load("image/Achille.png")
    AchilleImage = pygame.transform.scale(AchilleInit, (20, 20))
    TortueInit = pygame.image.load("image/Tortue.png")
    TortueImage = pygame.transform.scale(TortueInit, (20, 20))

    # boucle for pygame
    while running:
        screen.fill((255, 255, 255))
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
        line_maker(screen, step, AchilleImage, TortueImage)

        pygame.display.flip()


if __name__ == "__main__":
    main_achille_et_la_tortue()
    # run_achille_tortue(20)
