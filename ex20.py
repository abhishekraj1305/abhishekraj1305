from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

currnt_file = open(input_file)

print("first let's print the whole file:\n")

print_all(currnt_file)

print("now let's rewind, kind of people like a tape.")

rewind(currnt_file)

print("let's print three lines:")

current_line = 1
print_a_line(current_line,currnt_file)

current_line = current_line + 1
print_a_line(current_line, currnt_file)

current_line = current_line + 1
print_a_line(current_line, currnt_file)
