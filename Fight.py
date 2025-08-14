import random
import sys

def fight(CoolGuyhp, opName, opHP, opDMG1, opDMG2, CoolGuydmg1, CoolGuydmg2, CheckDMG, Inventory RunAwayMessageFail, RunAwayMessagePass, coin):
    MonsterLifeStatus = True #True #= #ALIVE #:O
    while(True):
        if CoolGuyhp <= 0:
            print ("YOU DIED")
            sys.exit()
            
        elif opHP <= 0:
            print("The monster has 4 HP. You get ready for the last attack until...\nHe runs away")
            coin=coin+4
            print("\nYou got 4 coins")
            break
        print("You have",HealthBarP,"HP")
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Run away\n"))

        DodgeFlag=random.randint(0,10)
        PlayerDamage=random.randint(6,12)
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
        
        MonsterDamage=round(random.uniform(4,8.5),1)
        DodgePlayerFlag=random.randint(0,10)
        if(DodgePlayerFlag >= 2):
            HealthBarP=HealthBarP-MonsterDamage
            HealthBarP=round(HealthBarP,1)
            print('You took',MonsterDamage,'damage!')
        else:
            print('You dodged his attack')
        time.sleep(1)
    break
    coin = 0
    CoolGuyhp+=3
    return MonsterLifeStatus, Inventory, coin, CoolGuyhp