#sanke water game 
#snake drink water, gun shoots the snake and gun has no effect on water.

import random
list = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_point = 0
human_point = 0

print("\t \t \t \t snake, water, gun game\n")
print("s for snake \nw for water \ng for gun \n")

#making game in a while loop
while no_of_chance < chance:
    _input = input('snake, water,gun:')
    _random = random.choice(list)

    if _input == _random:
        print("tie both 0 point to each \n ")

    #if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "s" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print ("human_wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    #if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "w" and _random == "g":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print ("human_wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")    

    #if user enter g
    elif _input == "g" and _random == "s":
        computer_point = computer_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")

    elif _input == "g" and _random == "w":
        human_point = human_point + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print ("human_wins 1 point \n")
        print(f"computer_point is {computer_point} and your point is {human_point} \n")   

    else:
        print("you have input wrong \n")            

    no_of_chance = no_of_chance + 1
    print(f"chance - {no_of_chance} is left out of {chance} \n")

print("game over")

if computer_point == human_point:
    print("tie")

elif computer_point > human_point:
    print("computer wins and you loose")

else:
    print("you win and computer loose")    

print(f"your point {human_point} and computer point is {computer_point}")








