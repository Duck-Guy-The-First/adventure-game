import random
import sys
import time
def fight(CoolGuyhp, opName, opHP, opDMG1, opDMG2, opNum, CoolGuydmg1, CoolGuydmg2, Coolydodges1, Coolydodges2, DodgeFlag1, DodgeFlag2, pabol_and_bob, CheckDMG, inventory, RunAwayMessageFail, RunAway1, RunNum, RunAway2, RunAwayMessagePass):
    opLifeStatus = True #True #= #ALIVE #:O
    while(True):
        if CoolGuyhp <= 0:
            print ("YOU DIED")
            sys.exit()
            
        elif opHP <= 0:
            break
        print("You have",CoolGuyhp,"HP")
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Run away\n"))

        DodgeFlag=random.randint(DodgeFlag1,DodgeFlag2)
        CoolGuydamage=random.randint(CoolGuydmg1,CoolGuydmg2)
        RunAwayChance=random.randint(RunAway1,RunAway2)

        if(fight1==1):
            if(DodgeFlag >= opNum):
                opHP-=CoolGuydamage
                print("The ",opName," took",CoolGuydamage, "damage!")
            else:
                print("The",opName,"dodges your attak.")
        
        elif(fight1==2):
            print("The ",opName,"has",opHP,"HP. ",CheckDMG,".")
        
        elif(fight1==3):
            if(RunAwayChance > RunNum):                                                        
                print(RunAwayMessagePass)
                break
            else:
                print(RunAwayMessageFail)
        
        opDamage=random.uniform(opDMG1,opDMG2)
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
fight(100, "Monster", 34, 4, 10, 5, 13, 0, 10, 0, 10, "P&B", "He does little damage.", inventory , "You cooly dance so you can get past him...\n sadly he does not like dancing and gets mad. his damage increases by 0", 8, 8, 10,  "You see a butterfly in the sky and tell him.\nHe looks up and you see the oportunity to run away\nYou sneak past him.")
fight(100, "Caterpiller", 1, 1, 4, 1, 1000000, 1000000, 9, 10, 0, 10, "P&B", "He does little damage.", inventory, "You say that his wife and kids are dead.\nBut he dosn't believe you because they don't exist.", 9, 9, 10, "You put him on an other tree... You walk away as he screams at you still mad.")