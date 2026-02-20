import random
import sys
import time

def Bossfight(CoolGuyhp, opName, opHP, opDMG1, opDMG2, opNum, CoolGuydmg1, CoolGuydmg2, Coolydodges1, Coolydodges2, DodgeFlag1, DodgeFlag2, pabol_and_bob, CheckDMG, inventory):
    opLifeStatus = True #True #= #ALIVE #:O
    KPFlag=0
    KPActive = False
    while(True):
        if CoolGuyhp <= 0:
            print ("YOU DIED")
            sys.exit()
        elif opHP <= 0:
            break
        print("You have",CoolGuyhp,"HP")
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Inventory\n"))

        DodgeFlag=random.randint(DodgeFlag1,DodgeFlag2)
        CoolGuydamage = random.randint(CoolGuydmg1, CoolGuydmg2)
        if KPActive and KPFlag < 3:
            CoolGuydamage = int(CoolGuydamage * 1.25)
            KPFlag += 1
        if KPFlag >= 3:
            KPActive = False
            KPFlag = 0

        if(fight1==1):
            if(DodgeFlag >= opNum):
                opHP-=CoolGuydamage
                print("The ",opName," took",CoolGuydamage, "damage!")
            else:
                print("The",opName,"dodges your attack.")

        elif(fight1==2):
            print("The ",opName,"has",opHP,"HP. ",CheckDMG,".")

        elif(fight1==3):
            print("You have items:")
            num = 1
            for item, value in inventory.items():
                print("[",num,"]", item,":",value)
                num+=1
            print("B to go back")
            itemChoose = input("WHAT DO THY CHOOSE?\n")
            if(itemChoose == "1"):
                if (inventory["Health Potion"] == 0):
                    print("Thy don't have enough health potions!")
                else:
                    print("Thy used the health potion! Heals 17HP")
                    CoolGuyhp += 27
                    if(CoolGuyhp>=100):
                        CoolGuyhp = 100
            if(itemChoose == "2"):
                if (inventory["Broken Chat Filter"] == 0):
                    print("Thy don't have enough broken chat filters!")
                else:
                    badUse=int(input("This doesn't really work on boss fights. Use anyway?\n[1] I aint reading all that 😭😭😭😭😭😭😭😭😭 happy for you or sorry i don't care\n[2] I won't use it\n"))
                    if(badUse==1):
                        print("He looks at you with disappointment\n",pabol_and_bob,"")
            if(itemChoose == "3"):
                if (inventory["Killing Potion"] == 0):
                    print("Thy don't have enough killing potion!")
                elif not KPActive:
                    KPActive = True
                    KPFlag = 0
                    print("Thy have got more damage for 3 turns")
                else:
                    print("Killing Potion effect is already active") 
            if(itemChoose == "4"): 
                if (inventory["Walmart Shopping Bag"] == 0):
                    print("Why do thy thinks thy has this?")
                else:
                    print("You used the walmart shopping bag you now have")
                    time.sleep(4)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("No life")
                    time.sleep(3)
            continue
                        
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
    "Health Potion":0,
    "Broken Chat Filter":0,
    "Killing Potion":0,
    "Walmart Shopping Bag":0
}
Bossfight(100, "MeroDach", 143, 9, 28, 0, 17, 29, 0, 10, 10, 10, "Thy are stupid", "He does high damage", inventory)