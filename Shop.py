
def shop(coin,inventory):
    print("HELLO")
    while(True):
        ChooseShop=int(input("WHAT DO THY WANT FROM MY SHOP\n[1] Check\n[2] Buy\n[3] Leave\n"))
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
            # all coins for Walmart Shopping Bag
        elif(ChooseShop==2):
            while(True):
                print("Coins: ",coin)
                BuyOption=input("DO THY WANT [1] HEALTH POTION - 6 coins\nOR DO THY WANT MY [2] Broken chat filter - 8 coins\n OR DO THY WANT MY [3] KILLING POTION - 15 coins\nOR DO THY WANT MY [4] Walmart Shopping Bag - 1000 coins\n[B] Go back\n")
                if(BuyOption=="1" and coin>=6):
                    print("You got a health potion")
                    coin-=6
                    inventory["Health Potion"] += 1
                else:
                    print("IT SEEMS THAT THY DON'T A ENOUGH FOR A HEALTH POTION")
                if(BuyOption=="2" and coin>=8):
                    print("You got the broken chat filter")
                    coin-=8
                else:
                    print("IT SEEMS THAT YOU DON'T A ENOUGH FOR THE BROKEN CHAT FILTER")
                if(BuyOption=="3" and coin>=15):
                    print("You got a killing potion")
                    coin-=15
                else:
                    print("IT SEEMS THAT YOU DON'T A ENOUGH FOR A KILLING POTION")
                if(BuyOption=="4" and coin>=1000):
                    coin-=1000
                    print("HOW DID THY BUY THE WALMART SHOPING BAG?")
                else:
                    print("IT'S THE MOST EXPENSIVE ITEM WHY DO YOU THING YOU CAN'T BUY IT")
                if(BuyOption=="B"):
                    break
        elif(ChooseShop==3):
            break
        
        return coin, inventory

inventory = {
    "Health Potion":0,
    "Broken Chat Filter":0,
    "Killing Potion":0,
    "Walmart Shopping Bag":0
}

coin = 25
coin, inventory = shop(coin,inventory)