CaterpillarStatus=False
get_key=False
if(CaterpillarStatus==False):
    print("You see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, a coded locked door and your face on a wanted poster.")
else:
    print("You see a prison so you walk in and see a cop sleeping, a goblin, a toothbrush, and a... thing? in jail. you also see a locked door, and coded locked door")
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
            print('You walk up to the toothbrush "Can you please get out of here that cop hes been sleeping for 9 days and if he wakes up i will be trapped here with you.\nI do not want to be trapped here with you"')
        else:
            print('You walk up to the toothbrush "You see that cop? hes been sleeping for 9 days i do not know how?"')
    if(choose5==6):
        if(CaterpillarStatus==False):
            print('You walk up to the glitchy thing "2... i said a number now go away you caterpiller killer"')
        else:
            print('You walk up to the glitchy thing "Hi i need to say a number for you to play the game uhhhhhh\n2"')
        