print("""You enter a dark room with two door.
do you go through the door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("there's a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. take the cake.")
    print("2. scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face off. Good job!")
    elif bear == "2.":
        print("the bear eats your leg off. Good job!")    
    else:
        print(f" well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door  == "2" :    
    print("You stare into the endless abyss at cthulu's retina.") 
    print("1. blueberries") 
    print("2. Yellow jacket clothspins.")
    print("3. understanding revolvers yellig mrlodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello. ")
        print("good job!")
    else:  
        print("the insanity rots your eyes into a pool of muck.")  
        print("good job!")

else:
    print("you stumble around and fall on a knife and die. Good job!")  
    
