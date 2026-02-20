from threading import Timer
import time
import sys

CaterpillarStatus = False


def countdown():
    for i in range(seconds, 0, -1):
        print(f"\rDodge! Press enter ({i}).", end="", flush=True)
        time.sleep(1)
    print("\rYou were thrown in jail with the toothbrush!")


if __name__ == "__main__":
    print("You open the door.")
    time.sleep(1)
    print("You walk towards the exit but you hear some footsteps behide you and some lighting sounds")
    timeout = 3
    seconds = 3

    timer = Timer(timeout, countdown)
    timer.daemon = True
    timer.start()

    start_time = time.time()
    prompt = input(f"Dodge! Press enter ({seconds}).\n")
    timer.cancel()

    end_time = time.time()

    reaction_time = end_time - start_time
    if reaction_time < timeout:
        print("The police guard that was sleeping before tried to attack you with a taser but missed")
        dodged = True
    else:
        print("You get tased before getting thrown in jail with the toothbrush!")
        dodged = False

    chooseFree = int(input(
        "You look at the key that the cop dropped and look at the prisoners.\nWHAT DO THEY CHOOSE\n[1] Free the prisoners\n[2] Run out of the prison\n"))

    if (chooseFree == 1):
        print("You free the them...\nYou can help them but you killed the caterpiller so i still hate you.\nBut i guess the prisoners don't anymore.\nYour reputation increases by 2")
        rep = +2

    if (chooseFree == 2):
        print("You run out of the prison\nAre you just cold hearted?\nYour reputation decreases by 1")
        rep = -1
