from threading import Timer
import random
import sys
import tkinter as tk
from PIL import Image, ImageTk
import time


def showCompassImage():
    img = Image.open('Map.1.png')
    img = img.resize((950, 600))
    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

theForest = False
nearbyVillage = False
weirdCliff = False
twoDoors = False

choose7 = int(input(
    "WHAT DO THY Go\n[1] Go to the forest\n[2] Go to the nearby village\n[3] Go to a weird cliff\n[4] Go to the two doors\n[5] Check the compass\n[6] Use the cube\n"))
if (choose7 == 1):
    theForest = True
    print("You walk through the forest hoping that you don't die you look around for anything and then you see a deer on two legs.\nYou stare at it, it stares back until it runs away.")
    print("You continue walking around until you see a missing poster and draw a funny mustache on it before continuing on your way.\n")
if (choose7 == 2):
    nearbyVillage = True
    if (CaterpillarStatus == False):
        print("You go to the nearby village and everyone is hidding for some reason")
    else:
        print("You go to the nearby village and it's really peaceful, almost everyone is happy")
    chooseVillage1 = int(input(
        "WHAT DO THY CHOOSE\n[1] Explore the place\n[2] Continue on your way\n[3] Use the cube\n"))
    if (chooseVillage1 == 1):
        goVillage = int(input(
            "WHERE DO THY GO?\n[1] Go to the bus\n[2] Go to a back alley\n[3] Break into peoples houses (because for some reason that's normal in video games)\n[4] Continue on your way\n"))
        if (goVillage == 1):
            print('You go to the bus and see a bus driver sleeping. You check his pockets and find 5 coins and pocket the money, before waking him up. "Eh? Where do you want to go?" he asks and you think for a second')
            coin = coin+5
            chooseBus = int(input(
                "WHERE DO THY GO?\n[1] Go to your home town\n[B] Go back\n"))
            if (chooseBus == "1" and coin >= 8):
                
                rebuild = False
                CaterpillarStatus = False
                print('He reaches his hand out for the money and you give him 8 coins and you give him the money so he drives across the oceanto get you to the dirt road at the first island\nYou get out of the bus and he throws a button at you before driving away with no explanation because you are a terrible person after KILLING THE CATERPILLAR!!!!!!!!!!')
                print("You look around the area and see your destroyed house and the tree that you punched with the caterpiller's dead body to forever remind you of your sins")
            else:
                print('He reaches his hand out for the money and you give him 8 coins and you give him the money so he drives across the oceanto get you to the dirt road at the first island\nYou get out of the bus and he throws a button at you before driving away with no explanation because he doesn\'t care')
                print("You look around the area and see your destroyed house and the tree that you punched with the caterpiller just staring at you")
                
                if (rebuild == True):
                    chooseDR = int(input(
                        "WHAT DO THEY DO?\n[1] Go to your destroyed house\n[2] Go to the lake\n[3] Go to the mountain\n[4] Go to the tree\n[5] Get some wood\n"))
                else:
                    chooseDR = int(input(
                        "WHAT DO THEY DO?\n[1] Go to your destroyed house\n[2] Go to the lake\n[3] Go to the mountain\n[4] Go to the tree\n"))

                    if (chooseDR == 1):
                        print("You walk to your destroyed house and just stand there...\nBut then you get the idea to rebuild it.\n New quest: Rebuild your house")
                        rebuild = True

            if (chooseBus == "1" and coin < 8):
                print('"What do you mean you don\'t have enough money? Get out of the bus!" he throws you out of the bus')
                HealthBarP -= 5
                goVillage = int(input(
                    "WHERE DO THY GO?\n[1] Go to the bus\n[2] Go to a back alley\n[3] Break into peoples houses (because for some reason that's normal in video games)\n[4] Continue on your way\n"))
            elif (chooseBus == "B"):
                print('"Then why are you here? Go." You walk out of the bus.')
                goVillage = int(input(
                    "WHERE DO THY GO?\n[1] Go to the bus\n[2] Go to a back alley\n[3] Break into peoples houses (because for some reason that's normal in video games)\n[4] Continue on your way\n"))

if (choose7 == 3):
    weirdCliff = True
    print("")
if (choose7 == 4):
    twoDoors = True
    print("")
if (choose7 == 5):

    root = tk.Tk()
    root.title('Ics jpo sgd kafnn hnjsf5x? 2ngko fa 5gi!')
    root.geometry('1200x800')

    font = ('Comic Sans MS', 22)

    label = tk.Label(root, text='right 6', font=font)
    label.pack()

    button = tk.Button(root, text="check the map",
                       font=font, command=showCompassImage)
    button.pack()

    image_label = tk.Label(root)
    image_label.pack()

    root.mainloop()
choose7 = int(input(
    "WHAT DO THY Go\n[1] Go to the forest\n[2] Go to the nearby village\n[3] Go to the nearby cliff\n[4] Go to the two doors\n[5] Go to where the compass is pointing\n[6] Use the cube\n"))

if (choose7 == 6):
    print("You thorw the cube in the air and it starts floating. the walls start to fade away ones and zeros coming and going and soon you start to fade out of exi-01010100 01101000 01100101 01110010 01100101 00100000 01101001 01110011 00124848 24848484848484848484848484848484848484848485555555555555555555577777777777777777799999999999993333333332222222226666666666")
    coin, inventory = shop(coin, inventory)
    print("The shop keeper snaps his fingers and he disappears but suddenly 01010100 01101000 01100101 01110010 01100101 00100000 01101001 01110011")
choose7 = int(input(
    "WHAT DO THY Go\n[1] Go to the forest\n[2] Go to the nearby village\n[3] Go to the nearby cliff\n[4] Go to the two doors\n"))
