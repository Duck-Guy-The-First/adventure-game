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
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Inventory"))

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

        elif(fight1==3):
            print("You have items:")
            
            num = 1
            for item, value in inventory.items():
                print("[",num,"]", item,":",value)
                num+=1

            itemChoose = int(input("WHAT DO THY CHOOSE?"))
            if(itemChoose == 1):
                # Check if item is there or not
                if (inventory["Health Potion"] == 0):
                    print("You don't have enough health potions!")
                else:
                    print("You used the health potion! Heals 17HP")
                    
        opDamage=random.randint(opDMG1,opDMG2)
        dodgeCoolGuyflag=random.randint(Coolydodges1,Coolydodges2)
        if(dodgeCoolGuyflag >= 2):
            CoolGuyhp-=opDamage
            print('You took',opDamage,'damage!')
        else:
            print('You dodged his attack')
        time.sleep(1)
    CoolGuyhp+=3
    return opLifeStatus, inventory, CoolGuyhp

inventory = {
    "Health Potion":3,
    "Broken Chat Filter":1,
    "Killing Potion":1,
    "Walmart Shopping Bag":1
}
fight(100, "MeroDach", 67, 9, 28, 9, 8, 27, 0, 10, 0, 10, "B&P", "He does high damage", inventory)