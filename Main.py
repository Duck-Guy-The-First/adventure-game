from Shop import shop
import random
import sys
import tkinter as tk
from PIL import Image, ImageTk
import time
from playsound import playsound
def showImage():
    img = Image.open('Map-1.png')
    img = img.resize((800,700))
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

weapon=int(input('WHAT WEAPON DO THY CHOOSE?\n[1] Sword \n[2] Shield\n[3] Mace\n[5] A Bow And Arrow \n'))

charm=int(input("WHAT CHARM DO THY CHOOSE?\n[2] Crucifix \n[3] Amulet\n[4] A Weird Bottle\n[5] A Baby's Toy \n"))
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
    5:"A Bow And Arrow"
}
charmList = {
    2:"Crucifix",
    3:"Amulet",
    4:"A Weird Bottle",
    5:"A Baby's Toy",
    #1:"", leave the key for the code
}
coin = 7
rep = 2
HealthBarP = 100
print('your profile is\n')
print("Name:" ,name)
print('Race: ', raceList[race])
print('Weapon: ', weaponList[weapon])
print('Charm: ', charmList[charm])
print('Health Bar: ',HealthBarP)
print('Reputation: ',rep)
print("Coins: ",coin)
time.sleep(2)
if(raceList[race]=="Walmart Shopping Bag"):
    root = tk.Tk()
    root.title('The End')
    root.geometry('1413x945')

    font = ('Comic Sans MS',22)

    label=tk.Label(root,text='The Walmart Shopping Bag Ending',font = font)
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
        print("you hold up your fist and JUMPS THE AIR TO ATTACK MERODACH BUT he SLAPS YOU ON THE GROUND.\nOut of options, you run away, Merodach sees you running away but instead of chasing you his SMASHES YOUR HOME...")
    else:
        print('you get your wood sword and JUMP IN THE AIR TO ATTACK MERODACH BUT he grabs your sword and BREAKS IT IN PIECES.\nOut of options, you run away, Merodach sees you running away but instead of chasing you his SMASHES YOUR HOME...')
elif(choose2==2):
    print('You run away escaping merodach. Merodach sees you running away but instead of chasing you his SMASHES YOUR HOME')

print("Your running at somewhere you don't know, you stop running and check your surroundings and find you are somewhere far away from home.\n...\n(good)\nnot knowing where to go you find a compass on a log so you use it.")
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

    choose3=int(input('WHERE DO THY GO\n[1] Go to the crossed out area\n[2] Go back to the dirt road\n[3] Go to the cave\n'))
flag1=False
choose3_1=0
if(choose3==1):
    print("You go to the crossed out area and it is a lake.\nIt seems you don't have a boat so you look around.")
    if(choose1==1):
        print('But you hear something "Hey you there, come on over here! It is me Eveline", says the old lady from before. You tell her that you do not have a boat and\nshe says. "Well i have blueprints to make a boat" says Eveline so you take the blueprints and goto make the boat.')
    if(choose1==2):
        print('.')
        time.sleep(3)
        print('.')
        time.sleep(3)
        print('.')
        time.sleep(3)
        print('But you see nothing so you walk away.')
    flag1=True
    choose3_1=int(input("WHERE DO THY GO? part 2\n[1] Go back to the dirt road\n[2] Go to the cave\n"))
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

if(choose3==3 or choose3_1==2):
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
        coin=coin+11
        print("Sadly you got 11 coins... I hate you")
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
choose4=int(input("You make the boat.\nWHAT DO THY CHOOSE\n[1] Go to cave\n[2] Go to the lake\n"))
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
print("And start rowing the boat")
print("You see an island so you go over to it. You get out of the boat and see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail, a locked door and a code locked door")
get_key=False
while(True):    
    choose5=int(input("WHAT DO THY CHOOSE\n[1] Check the cop\n[2] Check the locked door\n[3] Check the coded locked door\n[4] Talk to the goblin\n[5] Talk to the toothbrush\n[6] talk to the thing\n"))
    if(choose5==1):
        print("You check the cop to see if he has the key. You check his pockets and nothing. You check his hat and you see the key is glued to his head why?...\nBecause the key is glued you  can't get it")
    if(choose5==2):
        if(get_key==True):
            if(CaterpillarStatus==False):
                print("You unlock the door but you sill can't unlock your way out of the underworld because you KILLED THE CATERPILLER.")
            else:
                print("You unlock the door.")
            break
        print("You look at the locked door. But you don't have a key so you can't Ǵ̷̴̶̶̷̢̤̘̬͖̹͔̲̭͔̤͖̝̫̉ͭ̓̀́́̓̈̇͂͌̉̀̐ͯ͒̎ͭ̕͡E͚͔͍̚͝Ṫ̨̧̠̙̱͙̝̲̬̠̘̩̩͍̱̹̾̈̾̊̓̈́ͯ̈̑̌ͣ̈́ͩ̈̊̀̀ͬ̋̕͘͢͞ O̷̴̡͖̰͈̻̳̩ͮͩ̀ͤ̾͊͊̈͆̓̏̓̚U̶̲̘̩̱̙̻͔̪̻ͯ̊͆ͦͭ̑̽́̔͛͟͜_ͦ_̶̙͇͖̮̟̔̿͂͛͌͊̕͠T̷͚̱̮͇̩̮̟̤͔͕̩̤͙̳̯̥̦̙ͬͮͧ̀͋ͣͪ̐͗͊̃ͥ͆̄͐ͩ̆͜͠͠͡ͅͅͅ_͙ͫ͘ ")
    if(choose5==3):
        code1=int(input("You look at the screen and think if what the code is\nWHAT IS THE CODE\n"))
        if(code1==592):
            get_key=True
            print("The key is in the room so you get the key")
        else:
            print("You got it wrong")
    if(choose5==4):
        if(CaterpillarStatus==False):
            print('You walk up to the green tooth goblin "I have been here for 5 months. I had a friend named Goblin he is cool another named Goblin.\nHe is not cool and a another named Bob we do not talk about Bob now go away you moster."')
        else:
            print('You walk up to the green tooth goblin "I have been here for 5 months. I had a friend named Goblin he is cool another named Goblin.\nHe is not cool and a another named Bob we do not talk about Bob."')
    if(choose5==5):
        if(CaterpillarStatus==False):
            print('You walk up to the toothbrush "Can you please get out of here that cop hes been sleeping for 9 days and i do not want to wake up.\nI do not want to be trapped here with you"')
        
            print('You walk up to the toothbrush "You see that cop? hes been sleeping for 9 days i do not know how?"')
    if(choose5==6):
        print('You walk up to the glitchy thing "Hi i need to say a number for you to play the game uhhhhhh\n2"')
        