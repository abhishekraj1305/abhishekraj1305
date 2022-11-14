""" # creating a string
print("hello abhishek raj")

#creating a addition of int variable
print(28 + 7)

# creating a sum of floating point number
print(26.6 + 39.5)

#creating a boolean
print(7>5)

cars = 25 """

""" for i in range(0, 30):
    if i>5:
        continue
    print(i) """

""" odd_numbers = []
for number in range (0, 1201):
    if (number%2!=0):
        odd_numbers.append(number)

print (odd_numbers)        """

""" my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.pop()
my_list.pop(1)
print(my_list) """

""" my_list = ['cat', 'dog', 'fish']
print('cat' in my_list) """

""" for i in range(5):
    print(i) """

""" x = 0
for x in range(5):
    if x == 3:
        continue
    print(x) """

""" string = 'pasta'
result = ''

for i in range(len(string) - 1, -1, -1):
    result += string[i]
print(result)  """   

""" lst = []
for i in range(2):
    for j in range(1, 3):
        lst.append(i * j)
print(lst) """

""" l = ['foo', 'bar', 'baz']
while len(l) > 3:
    print(d.pop())
print('Done.')
 """

""" for num in range(1, -5, -1):
    print(num, end=", ") """

""" num = 10
i = 9
if num % i == 1:
    print(num)
    break
 """

""" for index in range(0,10):
    print (index)    
    if index==3:
        break """


""" def fun1(num):
    return num + 25

fun1(5)
print(num)  """       

def add_two(x):
    x = x + 2
    print(x)
    
add_two(5)