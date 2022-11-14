def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract (a, b):
    print(f"SUBTRACT {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"MULTIPLYING {a} - {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("let's do some math with just function!")    

age = add (30, 5)
height = subtract(78, 4)
weight = multiply(90,2)
iq = divide(100, 2)

print (f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")


# A puzzle for the extra credit, type it anyway
print("here is a puzzle.")
what = add (age, subtract(height, multiply(weight, divide(iq, 2))))

print("that become: ", what, "can you do it by hand?")
