from sys import exit

def gold_room():
    print("this room is full of gold. How much do you take?")

    choice = input("> ")
    if "o" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead ("man learn to type a number")    

    if how_much < 50:
        print("nice, you're not a greedy, you win!")
        exit(0)
    else:
        dead("you greedy bastard")  


def bear_room():
    print("there is a bear here.")         
    print("The bear has a bunch of honey.")
    print("the fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take money":
            dead("the bear looks at you then slaps your face off.")
        elif choice == "Taunt bear" and not bear_moved:
            print("The bear has moved from the door")   
            print("you can go through it now.")
            bear_moved = True
        elif choice == "Taunt bear" and bear_moved:
            dead("The bear  gets pissed off and chews of your legs off.")  
        elif choice == "open door" and bear_moved:
            gold_room()
        else: 
            print("I got no ideas what does that means")


def cthulhu_room():
    print("here you see the great evil cthulhu")
    print("He, it, whatever stears at you and you go insane")
    print("do you flee for your life or eat ypu head.")

    choice = input("> ")

    if "Flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")    
    else:
        cthulhu_room()


def dead(why):
    print(why, "good job!")        
    exit (0)

def start ():
    
    print("You are in a dark room.")           
    print("There is door to your left and right")
    print("whoch one do you take ?")

    choice = input (">")

    if choice == "left":
       bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("you stamble around the room until you starve")       


start()        