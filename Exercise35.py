#Branches and Functions

from sys import exit

def gold_room():
    print("This room is made of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a lot of honey")
    print("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your leg off.")
        elif choice == "open_door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that's tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door on your left and right.")
    print("Which door do you want to take.")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


