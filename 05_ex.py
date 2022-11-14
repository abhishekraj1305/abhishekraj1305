text = input("enter your text here: ")
if("harry" in text):
    print("yes! the text contain the name Harry")
elif("HARRY" in text):
    print("yes! the text contain the name Harry") 
elif("Harry" in text):
    print("yes! the text contain the name Harry")
elif("HaRRy" in text):
    print("yes! the text contain the name Harry")           
else:
    print("No! the text dosen't contain name Harry")  
