def shop(coin,inventory):
    print("HELLO")
    while(True):
        ChooseShop=input("WHAT DO THY WANT FROM MY SHOP\n[1] Check\n[2] Buy\n[3] Leave\n")
        if(ChooseShop=="1"):
            while(True):
                CheckOption=input("DO THY WANT TO CHECK MY [1] HEALTH POTION\nOR DO THY WANT TO CHECK MY [2] Broken chat filter\nOR DO THY WANT TO CHECK MY [3] KILLING POTION\nOR DO THY WANT TO GO BACK [B]\n")
                if(CheckOption=="1"):
                    print("THIS HEALTH POTION HEALS THY VERY GOOD CHOICE I MUST SAY.")
                elif(CheckOption=="2"):
                        print("THAT IS A BROKEN CHAT FILTER THAT I FOUND IN AGE OF EMPIRES II.\nIT MIGHT SEEM BAD BUT IT CAN INSULT THY ENEMIES MAKING THEM RUN AWAY CRYING AND FOR THE BATTLE END.\nIT IS SOMETHING THY NEED")
                elif(CheckOption=="3"):
                    print("THIS POTION TURNS THY IN TO A KILLING MACHINE IT GIVES THY MORE DAMAGE IN A BATTLE FOR 3 TURNS. I WOULD 100% RECOMMEND IT.")
                elif(CheckOption=="B"):
                    break
                else:
                    print("That does not exist mortal")
            # all coins for Walmart Shopping Bag
        elif(ChooseShop=="2"):
            while(True):
                print("Coins: ",coin)
                BuyOption=input("DO THY WANT [1] HEALTH POTION - 6 coins\nOR DO THY WANT MY [2] Broken chat filter - 8 coins\n OR DO THY WANT MY [3] KILLING POTION - 14 coins\nOR DO THY WANT MY [4] Walmart Shopping Bag - 1000 coins\n[B] Go back\n")
                if(BuyOption=="1"):
                    if(coin>=6):
                        print("Health potion has been added to your inventory")
                        coin-=6
                        inventory["Health Potion"] += 1
                    else:
                        print("IT SEEMS THAT THY DON'T A ENOUGH FOR A HEALTH POTION")
                elif(BuyOption=="2"):
                    if(coin>=8):
                        print("Broken chat filter has been added to your inventory")
                        coin-=8
                        inventory["Broken Chat Filter"] += 1
                    else:
                        print("IT SEEMS THAT YOU DON'T A ENOUGH FOR THE BROKEN CHAT FILTER")
                elif(BuyOption=="3"):
                    if(coin>=14):
                        if(coin>=6):
                            print("Killing potion has been added to your inventory")
                            coin-=14
                            inventory["Killing Potion"] += 1
                    else:
                        print("IT SEEMS THAT YOU DON'T A ENOUGH FOR A KILLING POTION")
                elif(BuyOption=="4"):
                    if(coin>=1000):
                        coin-=1000
                        print("HOW DID THY BUY THE WALMART SHOPING BAG?")
                        inventory["Walmart Shoping Bag"] += 1
                    else:
                        print("IT'S THE MOST EXPENSIVE ITEM WHY DO YOU THINK YOU CAN'T BUY IT")
                elif(BuyOption=="B"):
                    break
                else:
                    print("That does not exist mortal")
        elif(ChooseShop=="3"):
            break
        else:
            print("That does not exist mortal")
    return coin, inventory

#coin, inventory = shop(coin,inventory)