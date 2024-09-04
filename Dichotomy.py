def throwingTheRock(step):
    speed= 4
    distance = 8
    time = 0
    time_by_step = 1
    #distance of the rock
    Drock = 0
    for i in range(step):
        Drock += speed * time_by_step
        time +=1
        speed = speed/2
        print(f"emplacement de la pierre : {Drock} , emplacement de l'arbre {distance}")

throwingTheRock(50)
