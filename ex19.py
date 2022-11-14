def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} chesses!")
    print(f"you have {boxes_of_crackers}boxes of crackers!")
    print("man that's enough for a party")
    print("get a blanket.\n")


print("we can just give the fuction number directly:") 
cheese_and_crackers(20,30)

print("OR, we can use variabe from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can do maths inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("we can combine the two, variabl and maths:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +10000)
