import time
CaterpillarStatus=True
choose5=0
choose5_1=0
get_key=False
if(CaterpillarStatus==False):
    print("You see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, a coded locked door and your face on a wanted poster.")
else:
    print("You see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, and coded locked door")
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
        while(True):
            code1=input("You look at the screen and think of what the code is\nWHAT IS THE CODE\n\nPress B to go back\n")
            if(code1=="B"):
                break
            elif(code1=="592"):
                print("You unlock the door and see a closet")
                OpenSeasame=int(input("WHAT DO THY CHOOSE\n[1] Open the closet\n[2] Go back"))
                if(OpenSeasame==1):
                    get_key=True
                    print("You open the closet and see a key. Key has added to your inventory")
                    break
                if(OpenSeasame==2):
                    break
            else:
                print("You got it wrong")
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
            print('You walk up to the glitchy thing "2... i said a number now go away you caterpiller killer"')
        else:
            print('You walk up to the glitchy thing "Hi i need to say a number for you to play the game uhhhhhh\n2"')
    if(choose5_1==4):
        print("You check the wanted poster it says wanted for killing a caterpiller.\nI can't kill you but i hope other people will.")
    time.sleep(2)