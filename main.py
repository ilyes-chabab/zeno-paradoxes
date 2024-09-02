import math


def achille_et_la_tortue():
    achille=1
    tortue=10
    print("#" * math.floor(achille) + "A" + "#"*((tortue-math.floor(achille))-1) + "T" + "#"*3)
    while achille < tortue:
        achille = tortue 
        tortue += achille*1,5
        print("#" * math.floor(achille) + "A" + "#"*((tortue-math.floor(achille))-1) + "T" + "#"*3)



if __name__ == "__main__":
    achille_et_la_tortue()