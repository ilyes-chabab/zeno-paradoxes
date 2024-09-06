import math 

def Shoot(step):
    Distance=11
    DArrow = 0
    speed = 1
    time=0
    time_by_step = 1
    LastDArrow= 0
    for i in range(step):
        print("#" * math.floor(DArrow) + "F" + "#"*((math.floor(Distance)-math.floor(DArrow))-1) + "C")
        DArrow += speed * time_by_step
        time+=1
        print(f"temps : {time}s , emplacement fleche : {DArrow} , cible : {Distance}")
        
        if DArrow == LastDArrow:
            break
            
        LastDArrow = DArrow
    
    return DArrow

Shoot(10)
