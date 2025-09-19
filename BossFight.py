import random
import sys
import time
def fight(CoolGuyhp, opName, opHP, opDMG1, opDMG2, opNum, CoolGuydmg1, CoolGuydmg2, Coolydodges1, Coolydodges2, DodgeFlag1, DodgeFlag2, pabol_and_bob, CheckDMG, inventory):
    opLifeStatus = True #True #= #ALIVE #:O
    while(True):
        if CoolGuyhp <= 0:
            print ("YOU DIED")
            sys.exit()
            
        elif opHP <= 0:
            break
        print("You have",CoolGuyhp,"HP")
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n"))

        DodgeFlag=random.randint(DodgeFlag1,DodgeFlag2)
        CoolGuydamage=random.randint(CoolGuydmg1,CoolGuydmg2)

        if(fight1==1):
            if(DodgeFlag >= opNum):
                opHP-=CoolGuydamage
                print("The ",opName," took",CoolGuydamage, "damage!")
            else:
                print("The",opName,"dodges your attack.")
        
        elif(fight1==2):
            print("The ",opName,"has",opHP,"HP. He does little damage.")
        
        opDamage=random.randint(opDMG1,opDMG2)
        dodgeCoolGuyflag=random.randint(Coolydodges1,Coolydodges2)
        if(dodgeCoolGuyflag >= 2):
            CoolGuyhp-=opDamage
            print('You took',opDamage,'damage!')
        else:
            print('You dodged his attack')
        time.sleep(1)
        break
    CoolGuyhp+=3
    return opLifeStatus, inventory, CoolGuyhp
inventory = {
    "Health Potion":0,
    "Broken Chat Filter":0,
    "Killing Potion":0,
    "Walmart Shopping Bag":0
}
fight(100, "MeroDach", 86, 9, 34, 9, 8, 27, 0, 10, 0, 10, "B&P", "He does high damage", inventory)