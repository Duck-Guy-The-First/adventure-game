from Shop import shop
import random
import sys
import tkinter as tk
from PIL import Image, ImageTk
import time
def showImage():
    img = Image.open('Map-1.png')
    img = img.resize((250,130))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo
def showWalmartImage():
    img = Image.open('1684145949851.jpg')
    img = img.resize((800,700))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

#The game is not finished sorry ):

print('Hello there :D')
print('welcome to THE ABYSS\n')

race=int(input('WHAT ARE THY?\n[1] Human \n[2] Goblin\n[3] Elf\n[4] Monster\n[6] Attack Helicopter\n'))

name = input("Enter your name: ")

weapon=int(input('WHAT WEAPON DO THY CHOOSE?\n[1] Sword \n[2] Shield\n[3] Mace\n[5] Bow And Arrow \n'))

charm=int(input("WHAT CHARM DO THY CHOOSE?\n[2] Crucifix \n[3] Amulet\n[4] A Weird Bottle\n[5] A Baby's Toy \n"))

drink=int(input("WHAT IS THY FAVORITE DRINK\n[1] Soda\n[2] Rat Water\n[3] Food\n[5] Snow White And The Seven Dwarfs Live Acion Tralier\n"))
#add villain mode
raceList = {
    1:"Human",
    2:"Goblin",
    3:"Elf",
    4:"Monster",
    5:"Walmart Shopping Bag",
    6:"Attack Helicopter",
}
weaponList = {
    1:"Sword",
    2:"Shield",
    3:"Mace",
    4:"A Baby",
    5:"Bow And Arrow"
}
charmList = {
    2:"Crucifix",
    3:"Amulet",
    4:"A Weird Bottle",
    5:"A Baby's Toy",
    #1:"", leave the key for the code
}
drinkList ={
    1:"Soda",
    2:"Rat Water",
    3:"Food",
    4:"Oil The Milky Edition",
    5:"Snow White And The Seven Dwarfs Live Acion Tralier",
}
coin = 7
inventory = {
    "Health Potion":0,
    "Broken Chat Filter":0,
    "Killing Potion":0,
    "Walmart Shopping Bag":0
}
rep = 2
HealthBarP = 100
print('your profile is\n')
print("Name:" ,name)
print('Race: ', raceList[race])
print('Weapon: ', weaponList[weapon])
print('Charm: ', charmList[charm])
print("Favorite Drink: ",drinkList[drink])
print('Health Bar: ',HealthBarP)
print('Reputation: ',rep)
print("Coins: ",coin)
time.sleep(2)
if(raceList[race]=="Walmart Shopping Bag"):
    root = tk.Tk()
    root.title('The End')
    root.geometry('1413x945')

    font = ('Comic Sans MS',22)

    label=tk.Label(root,text='The Walmart Shopping Bag Ending\nOk go play the actual game now instead of looking at this joke ending',font = font)
    label.pack()

    button=tk.Button(root,text="Walmart",font = font,command=showWalmartImage)
    button.pack()

    image_label = tk.Label(root)
    image_label.pack()

    root.mainloop()
    sys.exit()

print('\n------the story begins------\n')
print('\nOnce upon a time there was a',raceList[race],'living in the jungle, but there was a problem.\nA MONSTER was attacking the jungle and the animals.\nYou walk down a dirt road when you come across an old lady packing all her stuff as fast as shecould.')
choose1=int(input('"HELP THERES A MONSTER COMING AND I NEED HELP GETING MY STUFF IN MY CART", says the old lady.\nWHAT DO THY CHOOSE?\n[1] Help the old lady\n[2] Continue on your way\n'))

if(choose1==1):
    rep=rep+1
    print('You helped the old lady "Thank you young',raceList[race],'",says the old lady.\n your reputation increases by 1')
    print('"For you kindness i would like to give you my-... the map it is at the camp."You look at the camp and see a map. You run over to her camp and pick up her map and see a path to an ancient mountain...\nBut you ignore it for now and continue on your path.')
elif(choose1==2):
    rep=rep-1
    print('You walk away not carfing about the old lady.\nYour reputation decreases by 1')
    print('You see a camp in the distance and see a map there. You run over to the camp and pick up the map and see a path to an ancient mountain...\nBut you ignore it for now and continue on your path.')

print('you walk down the dirt path when you see THE MONSTER THE OLD LADY TALKING ABOUT. You name him Merodach, you name him after your English teacher\nMerodach ATTACKS YOU, you dodge his attack.')
choose2=int(input('WHAT DO THY CHOOSE \n[1] Attack \n[2] Run\n'))

if(choose2==1):
    if(raceList[race]=="Goblin"):
        print("you hold up your fist and JUMPS THE AIR TO ATTACK MERODACH BUT he SLAPS YOU IN THE AIR MAKING YOU FLY AWAY.\nMerodach sees you flying away but instead of chasing you his SMASHES YOUR HOME...")
    else:
        print('you get your wood sword and JUMP IN THE AIR TO ATTACK MERODACH BUT he grabs your sword and BREAKS IT IN PIECES.\nOut of options, you run away, Merodach sees you running away but instead of chasing you his SMASHES YOUR HOME...')
elif(choose2==2):
    print('You run away escaping merodach. Merodach sees you running away but instead of chasing you his SMASHES YOUR HOME')
if(raceList[race]=="Goblin"):
    if(choose2==1):
        print("You are in the sky until you hit the ground you start going back to fight Merodach until you find a compass and realize that you need to get stronger")
print("Your running at somewhere you don't know, you stop running and check your surroundings and find you are somewhere far away from home.\nNot knowing where to go you find a compass on a log so you use it.")
map=int(input('... you check the map\n[1] Do it\n'))
if(map==1):

    root = tk.Tk()
    root.title('RADHT IWT **** CDL')
    root.geometry('1200x800')

    font = ('Comic Sans MS',22)

    label=tk.Label(root,text='15',font = font)
    label.pack()

    button=tk.Button(root,text="check the map",font = font,command=showImage)
    button.pack()

    image_label = tk.Label(root)
    image_label.pack()

    root.mainloop()

    choose3=int(input('WHERE DO THY GO\n[1] Go to the crossed out area\n[2] Go back to the dirt road\n[3] Go to the cave\n[4] Go to where the compass was pointing\n'))
flag1=False
choose3_1=0
GoShop=False

while(True):
    if(choose3==1):
        if(choose1==1):
            print('You hear something "Hey you there, come on over here! It is me Eveline", says the old lady from before. You tell her that you do not have a boat and\nshe says. "Well i have blueprints to make a boat" says Eveline so you take the blueprints and goto make the boat.')
        if(choose1==2):
            print('.')
            time.sleep(3)
            print('.')
            time.sleep(3)
            print('.')
            time.sleep(3)
            print('But you see nothing so you walk away.')
        flag1=True
        choose3_1=int(input("WHERE DO THY GO (part 2)\n[1] Go back to the dirt road\n[2] Go to the cave\n[3] Go to where the compass was pointing\n"))
    if(choose3==2 or choose3_1==1):
        print("you walk to the dirt road you are almost at the dirt road when you see a MONSTER")
        HealthBarTutorial = 25

        while(True):
            if HealthBarP <= 0:
                print ("YOU DIED")
                sys.exit()
            
            elif HealthBarTutorial <= 0:
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
    if(choose3==3 or choose3_1==2):
        print("you walk to the cave and see a wall made out of ropes you try to untangle it... but you hear something")
        time.sleep(10)
        num = 10

        while num > 0:
            print(num)
            num = num - 1
            time.sleep(1.0)

        print("BOOM!")
        print('the cave blew up, KILLING YOU INSTANTLY\nThe bad ending')
        sys.exit()
    if(choose3==4 or choose3_1==3):
        if(GoShop==True):
            print("You walk back to the shop")
            coin, inventory = shop(coin,inventory)
            print("You walk back to where you were before")
        else:
            print("You walk into the bushes when you see...")
            coin, inventory = shop(coin,inventory)
            print("The shop owner thorws a red cube at you and you walk away going back to where you started\nSuper duper mini tiny shop (aka the cube) has been added to your inventory")
            GoShop=True
        if(flag1==True):
            choose3_1 = int(input("WHERE DO THY GO?\n[1] Dirt Road\n[2] Cave\n[3] Go back to the shop\n"))
        else:
            choose3 = int(input("WHERE DO THY GO?\n[1] Lake\n[2] Dirt Road\n[3] Cave\n[4] Go back to the shop\n"))
        

time.sleep(3)
print('You walk to the dirt road after the fight and see destroyed houses and dead people at the camp. You get the wood from the destroyed houses and go to your home.\nYour walking to your house and see that it is DESTROYED. In a fit of rage you punch a tree with the middle part breaking but the rest of it staying up.\nbut a caterpillar jumps out and says "YOU ARE DESTROYING MY HOME MAN" and he jumps at you')
HealthBarCaterpillar = 1
CaterpillarStatus=True
while(True):
    if HealthBarP <= 0:
        print ("YOU DIED")
        sys.exit()
    
    elif HealthBarCaterpillar <= 0:
        print("You kill the caterpillar what is wrong with you?")
        CaterpillarStatus=False
        coin=coin+32
        print("you got 32 coins... I hate you")
        break
    print("don't kill him if you're not terrible")
    print("You have",HealthBarP,"HP")
    fight1=int(input("WHAT DO THY CHOOSE?\n[1] Fight\n[2] Check\n[3] Run away\n"))

    DodgeFlag=random.randint(0,10)
    PlayerDamage=random.randint(10000,10000)
    RunAwayChance=random.randint(0,10)

    if(fight1==1):
        if(DodgeFlag >= 3):
            HealthBarCaterpillar=HealthBarCaterpillar-PlayerDamage
            print("The caterpillar took",PlayerDamage, "damage!")
        else:
            print("You missed and punched the tree and he gets mad")
    
    elif(fight1==2):
        print("The caterpillar has",HealthBarCaterpillar,"HP. He does little damage.")
    
    elif(fight1==3):
        if(RunAwayChance >= 9.5):
            print('You put him on an other tree... He is still mad and you walk away as he screams at you.')
            break
        else:
            print("You say that his wife and kids are dead.\nBut he dosn't believe you.")

    CaterpillarDamage=round(random.uniform(0.5,4.5),1)
    DodgePlayerFlag=round(random.uniform(9.5,10.0),1)

    if(DodgePlayerFlag >= 2):
        HealthBarP=HealthBarP-CaterpillarDamage
        print('You took',CaterpillarDamage,'damage!')
    else:
        print('He missed')
    time.sleep(1)
time.sleep(3)

if(CaterpillarStatus==False):
    rep=rep-1
else:
    rep=rep+1

if(CaterpillarStatus==False):
    print("You get wood and some duck tape after you KILLED THE CATERPILLAR YOU MONSTER so you try can make a boat")
else:
    print("You walk away from the caterpillar. You get the wood and some duck tape so you can try to make a boat.")
print("You put the materials on the floor in your destroyed home and start building a boat. You hear a buzzing sound and look up to see the sky gliching. You blink and it stops.")
time.sleep(1)
if(GoShop==True):
    choose4=int(input("You make the boat.\nWHAT DO THY CHOOSE\n[1] Go to cave\n[2] Go to the lake\n[3] Go back to the shop\n"))
else:
    choose4=int(input("You make the boat.\nWHAT DO THY CHOOSE\n[1] Go to cave\n[2] Go to the lake\n[3] Go to where the compass was pointing\n"))
if(choose4==1):
    print("you walk to the cave and see a wall made out of ropes you try to untangle it... but you hear something")
    time.sleep(10)
    num = 10

    while num > 0:
        print(num)
        num = num - 1
        time.sleep(1.0)

    print("BOOM!")
    print('the cave blew up, KILLING YOU INSTANTLY. the bad ending')
    sys.exit()
if(choose4==2):
    if(flag1==True):
        if(choose1==1):
            print("You go back to the lake it seems Eveline left the area but that does not matter right now so you put the boat on the water.")
        else:
            print("You go back to the lake and you put the boat on the water.")
    else:
        print("You go to the lake and you put the boat on the water.")
        if(choose4==3):
            if(GoShop==True):
                print("You walk back to the shop")
                coin, inventory = shop(coin,inventory)
                print("You walk back to where you were before")
            else:
                print("You walk into the bushes when you see...")
                coin, inventory = shop(coin,inventory)
                print("The shop owner thorws a red cube at you and you walk away going back to where you started\nSuper duper mini tiny shop (aka the cube) has been added to your inventory")
                GoShop=True

print("And start rowing the boat")
choose5=0
choose5_1=0
get_key=False
flag2=False
if(CaterpillarStatus==False):
    print("You see an island so you go over to it. You get out of the boat and see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, a coded locked door and your face on a wanted poster.")
else:
    print("You see an island so you go over to it. You get out of the boat and see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, and coded locked door")
while(True):
    if(CaterpillarStatus==False):
        choose5_1=int(input("WHAT DO THY CHOOSE\n[1] Check the cop\n[2] Check the locked door\n[3] Check the coded locked door\n[4] Check your wanted poster\n[5] Talk to the goblin\n[6] Talk to the toothbrush\n[7] talk to the thing\n"))
    else:
        choose5=int(input("WHAT DO THY CHOOSE\n[1] Check the cop\n[2] Check the locked door\n[3] Check the coded locked door\n[4] Talk to the goblin\n[5] Talk to the toothbrush\n[6] talk to the thing\n"))
    if(choose5==1 or choose5_1==1):
        print("You check the cop to see if he has the key. You check his pockets and nothing. You check his hat and you see the key is glued to his head why?...\nBecause the key is glued you  can't get it")
    if(choose5==2 or choose5_1==2):
        if(get_key==True):
            if(CaterpillarStatus==False):
                print("You unlock the door but you sill can't unlock your way out of the underworld because you KILLED THE CATERPILLER.")
            else:
                print("You unlock the door.")
            break
        print("You look at the locked door. But you don't have a key so you can't Ǵ̷̴̶̶̷̢̤̘̬͖̹͔̲̭͔̤͖̝̫̉ͭ̓̀́́̓̈̇͂͌̉̀̐ͯ͒̎ͭ̕͡E͚͔͍̚͝Ṫ̨̧̠̙̱͙̝̲̬̠̘̩̩͍̱̹̾̈̾̊̓̈́ͯ̈̑̌ͣ̈́ͩ̈̊̀̀ͬ̋̕͘͢͞ O̷̴̡͖̰͈̻̳̩ͮͩ̀ͤ̾͊͊̈͆̓̏̓̚U̶̲̘̩̱̙̻͔̪̻ͯ̊͆ͦͭ̑̽́̔͛͟͜_ͦ_̶̙͇͖̮̟̔̿͂͛͌͊̕͠T̷͚̱̮͇̩̮̟̤͔͕̩̤͙̳̯̥̦̙ͬͮͧ̀͋ͣͪ̐͗͊̃ͥ͆̄͐ͩ̆͜͠͠͡ͅͅͅ_͙ͫ͘ ")
    if(choose5==3 or choose5_1==3):
        if(flag2==True):
            if(get_key==True):
                print("it's a empty")
                time.sleep(2)
            else:
                while(True):
                    OpenSeasame=int(input("WHAT DO THY CHOOSE\n[1] Open the closet\n[2] Go back\n"))
                    if(OpenSeasame==1):
                        get_key=True
                        print("You open the closet and see a key. Key has added to your inventory")
                        break
                    if(OpenSeasame==2):
                        break
        elif(flag2==False):
            print("You look at the screen and think of what the code is")
            while(True):
                code1=input("WHAT IS THE CODE\n\nPress B to go back\n")
                if(code1=="B"):
                    break
                elif(code1=="592"):
                    flag2=True
                    print("You unlock the door and see a closet")
                    OpenSeasame=int(input("WHAT DO THY CHOOSE\n[1] Open the closet\n[2] Go back"))
                    if(OpenSeasame==1):
                        get_key=True
                        print("You open the closet and see a key. Key has added to your inventory")
                        break
                    if(OpenSeasame==2):
                        break
    if(choose5==4 or choose5_1==5):
        if(CaterpillarStatus==False):
            print('You walk up to the green tooth goblin "I have been here for 5 months. I had a friend named Goblin he is cool another named Goblin.\nHe is not cool and a another named Bob we do not talk about Bob now go away you moster."')
        else:
            print('You walk up to the green tooth goblin "I have been here for 5 months. I had a friend named Goblin he is cool another named Goblin.\nHe is not cool and a another named Bob we do not talk about Bob."')
    if(choose5==5 or choose5_1==6):
        if(CaterpillarStatus==False):
            print('You walk up to the toothbrush "Can you please get out of here that cop hes been sleeping for 9 days and if he wakes up i will be trapped here with you.\nI do not want to be trapped here with you"')
        else:
            print('You walk up to the toothbrush "You see that cop? hes been sleeping for 9 days i do not know how?"')
    if(choose5==6 or choose5_1==7):
        if(CaterpillarStatus==False):
            print('You walk up to the glitchy thing "2"')
        else:
            print('You walk up to the glitchy thing "Hi i need to say a number for you to play the game uhhhhhh\n2"')
    if(choose5_1==4):
        print("You check the wanted poster it says wanted for killing a caterpiller.\nI can't kill you but i hope other people will.")
print("You walk out of the prison but you look at the key. and then look at the others.")
choose6=int(input("WHAT DO THY CHOOSE\n[1] Free the others\n[2] Get out"))
if(choose6==1):
    if(CaterpillarStatus==False):
        print("You free the them...\nYou can help them but you killed the caterpiller.\nYour reputation increases by 1")
    else:
        print("You free the them.\nYour reputation increases by 2")
    rep=+2
if(choose6==2):
    if(CaterpillarStatus==False):
        print("You run out of the prison\nYou have no soul\nYour reputation decreases by 1")
    else:
        print("You run out of the prison\nYour reputation decreases by 1")
    rep=-1
if(weaponList[weapon]=="A Baby"):
    print("You see a log so you decide to take a break and sit down and think. When you see something  in to the mud crying.\nYou walk over to it and see a baby crying in the mud you start walking away until the baby teleports in your hand.\n A baby has been added to your weapons now you do more damage. Your sanity has dropped to zero. You name the baby disappointment. You see Merodach and get ready for a fight hoping that Disappointment can be a good weapon but Merodach walks past you to go destroy more towns.")
else:
    print("You see a log so you decide to take a break and sit down and think. When you see something embedded in to the ground.\nYou walk over there and see it is a ",weaponList[weapon]," so you try to pull it out of the ground until you see MERODACH.\nYou start running around panicking Merodach sees you but instead of attacking you he pulls out the ",weaponList[weapon]," and give it to you before he walks away to go destroy more towns.")
while(True):
    choose7=int(input("WHAT DO THY CHOOSE\n[1] Attack him\n[2] Let him walk away"))
    if(choose7==1):
        print("This opiton is still being worked on so maybe try the other opiton sorry :(")
    if(choose7==2):
        if(weaponList[weapon]=="A Baby"):
            print("You let him walk away not wanting to give Disappointment a concussion on the first fight")
        else:
            print("You let him walk away happy that you got the",weaponList[weapon],"and continue your journey")
    break
print("You walk around not knowing where your going and then realize that you need to THINK to survive :O")
choose8=int(input("WHAT DO THY Go\n[1] Go to the forest\n[2] Go to the nearby village\n[3] Go to the nearby cliff\n[4] Go to the two doors\n[5] Use the cube"))
if(choose8==1):
    print("")
if(choose8==2):
    print("")
if(choose8==3):
    print("")
if(choose8==4):
    print("")
if(choose8==5):
    print("You thorw the cube in the air and it starts floating. the walls start to fade away ones and zeros coming and going and soon you start to fade out of exi-01010100 01101000 01100101 01110010 01100101 00100000 01101001 01110011 00100000 01101110 01101111 01110111 00100000 01101110 01101111 01110100 01101000 01101001 01101110 01100111 00100000 01100010 01110101 01110100 00100000 01110100 01101000 01100101 00100000 01100101 01101101 01110000 01110100 01111001 00100000 01100010 01101100 01100001 01100011 01101011 00100000 01110110 01101111 01101001 01100100 00101110 00100000 01001110 01100101 01111000 01110100 00100000 01100100 01100101 01110011 01110100 01101001 01101110 01100001 01110100 01101001 01101111 01101110 00100000 01110100 01101000 01100101 00100000 01110011 01101000 01101111 01110000\n You are in a weird forest an see the shop")
    coin, inventory = shop(coin,inventory)
    print("The shop keeper snaps his fingers and he disappears but suddenly 01010100 01101000 01100101 01110010 01100101 00100000 01101001 01110011 00100000 01101110 01101111 01110111 00100000 01101110 01101111 01110100 01101000 01101001 01101110 01100111 00100000 01100010 01110101 01110100 00100000 01110100 01101000 01100101 00100000 01100101 01101101 01110000 01110100 01111001 00100000 01100010 01101100 01100001 01100011 01101011 00100000 01110110 01101111 01101001 01100100 00101110 00100000 01001110 01100101 01111000 01110100 00100000 01100100 01100101 01110011 01110100 01101001 01101110 01100001 01110100 01101001 01101111 01101110 00111010 00100000 01000100 01101001 01101101 01100101 01101110 01110011 01101001 01101111 01101110 00100000 00110010 00110000 00110110 00110011\n... you are back where you were before")
choose8=int(input("WHAT DO THY Go\n[1] Go to the forest\n[2] Go to the nearby village\n[3] Go to the nearby cliff\n[4] Go to the two doors\n[5] Use the cube"))
