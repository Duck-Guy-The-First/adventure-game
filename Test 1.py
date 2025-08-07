flag2=False
get_key=False
if(flag2==True):
            if(get_key==True):
                print("it's a empty")
            OpenSeasame=int(input("WHAT DO THY CHOOSE\n[1] Open the closet\n[2] Go back\n"))
            if(OpenSeasame==1):
                    get_key=True
                    print("You open the closet and see a key. Key has added to your inventory")
                    break
                if(OpenSeasame==2):
                    break
            while(True):
                code1=input("You look at the screen and think of what the code is\nWHAT IS THE CODE\n\nPress B to go back\n")
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
                else:
                    print("You got it wrong")