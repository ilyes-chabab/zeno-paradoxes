import math

# suite convergeante = u de n = 1:n
def Da_et_la_Dt():

    Da=1
    Dt=100
    t=1
    Va= Dt/ t
    Vt= 2
    # print("#" * math.floor(Da-1) + "A" + "#"*((Dt-math.floor(Da))-1) + "T" + "#"*3)
    for i in range(4):
        t+=1
        Da += Va * t
        Dt += Vt * t
        # print("#" * math.floor(Da) + "A" + "#"*((math.floor(Dt)-math.floor(Da))-1) + "T" + "#"*3)
        print("temps : " ,t ,"distance achille : " , Da , "distance tortue", Dt)
        


if __name__ == "__main__":
    Da_et_la_Dt()