from sys import argv

script, filename = argv 

print(f"we are going to erase {filename}.")
print("if you don't want, that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

input("?")

print("opening the file....")
target = open (filename, 'w')

print("Trauncating the file. goodbye!")
target.truncate()

print("Now i'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print ("I' going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()