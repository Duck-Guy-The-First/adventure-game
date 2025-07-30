def shop(coin,inventory):
    print("HELLO")
    while(True):
        ChooseShop=int(input("WHAT DO THY WANT FROM MY SHOP DO THY WANT TO CHECK OR BUY MY ITEMS\n[1] Check\n[2] Buy\n[3] Leave\n[4] Steal\n"))
        if(ChooseShop==1):
            while(True):
                CheckOption=input("DO THY WANT TO CHECK MY [1] HEALTH POTION\nOR DO THY WANT TO CHECK MY [2] Broken chat filter\nOR DO THY WANT TO CHECK MY [3] KILLING POTION\nOR DO THY WANT TO GO BACK [B]\n")
                if(CheckOption=="1"):
                    print("THIS HEALTH POTION GIVES THY 17 HP. VERY GOOD CHOICE I MUST SAY.")
                if(CheckOption=="2"):
                        print("THAT IS A BROKEN CHAT FILTER THAT I FOUND IN AGE OF EMPIRES II.\nIT MIGHT SEEM BAD BUT IT CAN INSULT THY ENEMIES MAKING THEM RUN AWAY CRYING AND FOR THE BATTLE END.\nIT IS SOMETHING THY NEED")
                if(CheckOption=="3"):
                    print("THIS POTION TURNS THY IN TO A KILLING MACHINE IT GIVES THY 15% MORE DAMAGE IN A BATTLE FOR 3 TURNS. I WOULD 100% RECOMMEND IT.")
                if(CheckOption=="B"):
                    break
    
        elif(ChooseShop==2):
            while(True):
                BuyOption=int(input("DO THY WANT [1] HEALTH POTION - 6 coins\nOR DO THY WANT MY [2] Broken chat filter - 7 coins\n OR DO THY WANT MY [3] KILLING POTION - 15 coins\nOR DO THY WANT MY [4] Walmart Shopping Bag - 1000"))
            # all coins for Walmart Shopping Bag
        elif(ChooseShop==3):
            break
shop(coin=25,inventory=25)