ten_things = "apple orange cow telephone Lighht sugar"

print("wait there are not 10 things in that list. let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["day", "Night", "Song", "fribsee",
              "corn", "banana", "girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now")

print("there we go:", stuff)

print("let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #super cool
print('#'.join(stuff[3:5])) #super stealer
