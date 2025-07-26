def shop(coin,inventory):
    ChooseShop=int(input("HELLO WHAT DO THY WANT FROM MY SHOP DO THY WANT TO CHECK OR BUY MY ITEMS\n[1] Check\n[2] Buy\n[3] Steal\n"))
    if(ChooseShop==1):
        CheckOption=int(input(""))
    elif(ChooseShop==2):
        BuyOption=int(input("DO THY WANT [1] HEALTH POTION - 6 coins\nOR DO THY WANT MY [3] Broken chat filter - 7 coins\n OR DO THY WANT MY [2] KILLING POTION - 15 coins\nOR DO THY WANT MY [4] Walmart Shopping Bag - 1000"))
        # all coins for Walmart Shopping Bag