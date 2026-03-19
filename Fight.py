import random
import sys
import time


def fight(CoolGuyhp, opName, opHP, opDeath, opDMG1, opDMG2, opNum, CoolGuydmg1, CoolGuydmg2, Coolydodges1, Coolydodges2, DodgeFlag1, DodgeFlag2, pabol_and_bob, CheckDMG, inventory,
           RunAwayMessageFail, RunAway1, RunNum, RunAway2, RunAwayMessagePass):
    opLifeStatus = True #True #= #ALIVE #:O
    KPFlag = 0
    KPActive = False
    meanie = 5
    depression = 0
    while(True):
        if CoolGuyhp <= 0:
            print ("YOU DIED")
            sys.exit()
            
        elif opHP <= 0:
            
            break

        if opHP <= 0:
            print(opDeath)
            break

        print("You have",CoolGuyhp,"HP")
        fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Inventory\n[4] Run away\n"))

        DodgeFlag=random.randint(DodgeFlag1,DodgeFlag2)
        CoolGuydamage=random.randint(CoolGuydmg1,CoolGuydmg2)
        RunAwayChance=random.randint(RunAway1,RunAway2)

        # apply Killing Potion boost for up to 3 attacks
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
                print("The",opName,"dodges your attak.")
                meanie += 3
        elif(fight1==2):
            print(opName,"has",opHP,"HP. ",CheckDMG,".")
        
        elif(fight1==3):
            print("WHAT DO THY CHOOSE?")
            num = 1
            for item, value in inventory.items():
                print("[",num,"]", item,":",value)
                num+=1
            print("B to go back")
            itemChoose = input("WHAT DO THY CHOOSE?\n")
            if(itemChoose == "1"):
                if (inventory["Health Potion"] == 0):
                    print("THY DON'T HAVE ENOUGH HEALTH POTIONS!")
                else:
                    print("Thy used the health potion! Heals 17HP")
                    CoolGuyhp += 27
                    if(CoolGuyhp>=100):
                        CoolGuyhp = 100
            if(itemChoose == "2"):
                if (inventory["Broken Chat Filter"] == 0):
                    print("THY DON'T HAVE ENOUGH BROKEN CHAT FILTERS!")
                else:
                    beMeanie = input(f"THY USE BROKEN CHAT FILTER, CHOOSE AN INSULT\nmeanie points: {meanie}\n[1 You weird (need 7 meanie points)|2 You are a potato (need 10 meanie points)|3 You got square brain (need 14 meanie points)]\n[4 Your dad is a rock (need 18 meanie points)|5 What 9 + 10? (need 21 meanie points)|6 You are a noob (need 27 meanie points)]\n[7 You are old (need 32 meanie points)| 8 You are ugly (need 39 meanie points)| 9 Your single (need 46 meanie points)]\nB to go back\n")
                    
                    if beMeanie == "1":
                        if meanie >= 5:
                            print(opName,"looks at you a bit sad.\n depression increases by 2")
                            depression += 2
                            meanie -= 5
                        else:
                            print("THY IS BROKE!.. ON INSULTS!")
                    
                    elif beMeanie == "2":
                        if meanie >= 9:
                            print(opName,"looks at you confused.\n depression increases by 3")
                            depression += 3
                            meanie -= 9
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "3":
                        if meanie >= 14:
                            print(opName,"looks at you mad. very offensive!\n depression increases by 7")
                            depression += 7
                            meanie -= 14
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "4":
                        if meanie >= 18:
                            print(opName,"looks at you like you are a rock.\n depression increases by 14")
                            depression += 14
                            meanie -= 18
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "5":
                        if meanie >= 21:
                            print(opName,"looks at you with tears as he doesn't know the answer.\n depression increases by 14")
                            depression += 14
                            meanie -= 21
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "6":
                        if meanie >= 27:
                            print(opName,"gets sad that he has no b-.\n depression increases by 17")
                            depression += 17
                            meanie -= 27
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "7":
                        if meanie >= 32:
                            print(opName,"gets close to sobbing after getting called a noob.\n depression increases by 23")
                            depression += 23
                            meanie -= 32
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "8":
                        if meanie >= 40:
                            print(opName,"back gets worse.\n"+opName+"'s depression increases by 28, plus 100 back pain")
                            depression += 28
                            meanie -= 40
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "9":
                        if meanie >= 47:
                            print(f"{opName} cries a bit as he is single.\n depression increases by 36")
                            depression += 36
                            meanie -= 47
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    
                    elif beMeanie == "Your mama" or beMeanie == "your mama" or beMeanie == "Your Mama" or beMeanie == "your Mama" or beMeanie == "Yourmama" or beMeanie == "yourmama" or beMeanie == "YourMama" or beMeanie == "yourMama":
                        choose = int(input("THIS INSULT COSTS 100 MEANIE POINTS, CAN YOU USE IT?\n[1] Yes\n[2] No\n"))
                        if choose == 1:
                            meanie -= 100
                            print(f"You have gone too far as {opName} remembers his mama.\ndepression increases by 10000")
                            depression += 10000
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                    elif choose == 2:
                        print("THY DOESN'T USE IT!")
                        beMeanie = input(f"THY USE BROKEN CHAT FILTER, CHOOSE AN INSULT\nmeanie points: {meanie}\n[1 You weird (need 7 meanie points)|2 You are a potato (need 10 meanie points)|3 You got square brain (need 14 meanie points)]\n[4 Your dad is a rock (need 18 meanie points)|5 What 9 + 10? (need 21 meanie points)|6 You are a noob (need 27 meanie points)]\n[7 You are old (need 32 meanie points)| 8 You are ugly (need 39 meanie points)| 9 Your single (need 46 meanie points)]\nB to go back\n")

                    elif beMeanie == "Your mom" or beMeanie == "your mom" or beMeanie == "Your Mom" or beMeanie == "your Mom" or beMeanie == "Yourmom" or beMeanie == "yourmom" or beMeanie == "YourMom" or beMeanie == "yourMom":
                        choose = int(input("THIS INSULT COSTS 100 MEANIE POINTS, CAN YOU USE IT?\n[1] Yes\n[2] No\n"))
                        if choose == 1:
                            meanie -= 100
                            print(f"You have gone too far as {opName} remembers his mom.\n depression increases by 10000")
                            depression += 10000
                        else:
                            print("THY DON'T HAVE ENOUGH MEANIE POINTS!")
                        if choose == 2:
                            print("THY DOESN'T USE IT!")
                            beMeanie = input(f"THY USE BROKEN CHAT FILTER, CHOOSE AN INSULT\nmeanie points: {meanie}\n[1 You weird (need 7 meanie points)|2 You are a potato (need 10 meanie points)|3 You got square brain (need 14 meanie points)]\n[4 Your dad is a rock (need 18 meanie points)|5 What 9 + 10? (need 21 meanie points)|6 You are a noob (need 27 meanie points)]\n[7 You are old (need 32 meanie points)| 8 You are ugly (need 39 meanie points)| 9 Your single (need 46 meanie points)]\nB to go back\n")

                    elif beMeanie == "B" or beMeanie == "b":
                        for item, value in inventory.items():
                            print("[",num,"]", item,":",value)
                            num+=1


            if(itemChoose == "3"):
                if (inventory["Killing Potion"] == 0):
                    print("THY DON'T HAVE ENOUGH KILL POTIONS!")
                elif not KPActive:
                    KPActive = True
                    KPFlag = 0
                    meanie += 1
                    print("THY USED THE KILLING POTION!\nYou will do more damage for 3 turns!")
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


        elif(fight1==4):
            # success when random chance is >= threshold
            if RunAwayChance >= RunNum:
                print(RunAwayMessagePass)
                break
            else:
                print(RunAwayMessageFail)
        
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
# Move runnable code under this guard so import no longer triggers it
if __name__ == "__main__":
    # demo / test code here
    fight(100, "Monster", 34, "He is at 4 HP but jumps tawords the bushs where you lose Monster", 4, 11, 5, 6, 13, 0, 10, 0, 10, "P&B", "He does little damage.", inventory, "You danced cooly to get past him...\n he doesn't care", 0, 7, 10, "You see a butterfly in the sky and tell him.\n He looks up and you run past him, sneaking away.")
    fight(100, "Sleeply Cop", 53, "The fight goes for so long that the Sleeply Cop gets tired and falls asleep", 9, 29, 5, 6, 13, 0, 10, 0, 10, "P&B", "He does medium damage", inventory, "You point at the prison and say that it is a prisoners to distraction him.\nHe doesn't look away from you.", 0, 7, 10, "You throw a neckpillow at the Sleeply Cop and he falls asleep.")