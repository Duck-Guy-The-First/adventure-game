import time
import random
import sys
HealthBarTutorial = 35
HealthBarP = 100

while(True):
    if HealthBarP <= 0:
        print ("HAHAHAHAHAHHAHHAHAHHAHAHAHAHAHHAHAHAHAHHAHAHHAHA YOU DIED YOU DUMB DUMB LOL NOOB")
        sys.exit()
    
    elif HealthBarTutorial <= 0:
        print("The monster has 4 HP. You get ready for the last attack until...\nHe runs away")
        break
    print("You have",HealthBarP,"HP")
    fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Run away\n"))

    DodgeFlag=random.randint(0,10)
    PlayerDamage=random.randint(6,13)
    RunAwayChance=random.randint(0,10)

    if(fight1==1):
        if(DodgeFlag >= 3):
            HealthBarTutorial=HealthBarTutorial-PlayerDamage
            print("The monster took",PlayerDamage, "damage!")
        else:
            print("The monster dodges your attak.")
    
    elif(fight1==2):
        print("The monster has",HealthBarTutorial,"HP. He does little damage.")
    
    elif(fight1==3):
        if(RunAwayChance > 8):
            print('You convince that there is a butterfly in the sky.\nHe looks up and you sneak past him.')
            break
        else:
            print("You tried to convince him that there is a butterfly in the sky.\nBut it doesn't work.")
    
    MonsterDamage=random.randint(5,9)
    DodgePlayerFlag=random.randint(0,10)

    if(DodgePlayerFlag >= 2):
        HealthBarP=HealthBarP-MonsterDamage
        print('You took',MonsterDamage,'damage!')
    else:
        print('You dodged his attack')
    time.sleep(1)