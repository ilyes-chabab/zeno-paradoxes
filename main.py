import math
import pygame

# suite convergeante = u de n = 1:n
def Da_et_la_Dt(step):
    
    Da=2
    Dt=502
    ecart = Dt - Da
    temps_total=1
    temps_par_etape =1
    Vt= 500
    
    # print("#" * math.floor(Da-1) + "A" + "#"*((Dt-math.floor(Da))-1) + "T" + "#"*3)
    for i in range(step):
        Vt=Vt/2
        temps_total+=temps_par_etape
        Da = Dt
        Dt += Vt * temps_par_etape
        
        # print("#" * math.floor(Da) + "A" + "#"*((math.floor(Dt)-math.floor(Da))-1) + "T" + "#"*3)
        print("temps : " ,temps_total ,"distance achille : " , Da , "distance tortue", Dt)
        ecart = Dt - Da
    return Da , Dt , ecart

def line_maker(screen,step,imageA,imageT):
    x1=80
    x2=1200
    y=180
    n=0
    for i in range(step):
        Da,Dt,ecart=Da_et_la_Dt(n)
        pygame.draw.line(screen,(0,0,0),(x1,y) ,(x2,y), 2)
        # message(screen,20,"T",(Da,y,0,0),(0,0,0))
        screen.blit(imageA,(Da+x1,y))
        screen.blit(imageT,(Dt+x1,y))
        message(screen,20,f"ecart : {ecart} pixels",(0,y-25),(0,0,0))
        y+= 50
        n+=1
    
#fonction pour pouvoir ecrire quelque chose sur l'ecran
def message(screen,size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)

def main_achille_et_la_tortue():
    
    # init
    pygame.init()
    running=True
    start=False
    step=8
    screen = pygame.display.set_mode((1200,600))
    

    AchilleInit=pygame.image.load("image/Achille.png")
    AchilleImage=pygame.transform.scale(AchilleInit,(20,20))
    TortueInit=pygame.image.load("image/Tortue.png")
    TortueImage=pygame.transform.scale(TortueInit,(20,20))

    while running:
        screen.fill((255,255,255))
        message(screen,40,"Paradoxe d'Achille et la Tortue",(400,0,0,0),(0,0,0))
        message(screen,25,"temps par ligne : 1s , distance total : 1120 pixels ,vitesse initial d'Achille et de la Tortue' : 1000 et 500 pixels par seconde ",(10,100,0,0),(0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                start=True
        if start:
            line_maker(screen,step,AchilleImage,TortueImage)
        if not start:
            message(screen,25,"Appuyez sur n'importe quelle touche pour afficher la simulation",(350,55,0,0),(0,0,0))
            
             
            
    
        pygame.display.flip()



        


# if __name__ == "__main__":
main_achille_et_la_tortue()
# Da_et_la_Dt(20)