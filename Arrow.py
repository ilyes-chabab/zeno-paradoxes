import math


def Shoot(step):
    Distance = 100
    DArrow = 0
    speed = 40
    time = 0
    time_by_step = 1
    LastDArrow = 0
    for i in range(step):
        DArrow += speed * time_by_step
        speed /= 2
        time += 1
        print(f"temps : {time}s , emplacement fleche : {DArrow} , cible : {Distance}")
        if DArrow == LastDArrow:
            break

        LastDArrow = DArrow

    return DArrow


Shoot(200)
