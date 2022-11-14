#write a program to check given username contin 10 lettr or not

""" username = input("enter your name here\n")
if(len(username)<10):
    print("username has less than 10 character")
else:
    print("username has more than 10 character") """


#program to draw half diamond like structure
""" n = 9
for i in range (9):
    print (" " * (n-i-1), end="")
    print ("*" * (2*i+1), end="")
    print (" " * (n-i-1)) """



#python test, answer = 7
""" print(int(6==6.0)*3+4%5) """

#programm to type a multiplicatio table
#num = int(input("enter your nubmer\n"))
#for i in range (1, 21):
    #print(str(num) + "x" + str(i) + "=" + str(i*num))
    #print(f"{num}x{i}={num*i}")

""" def maximum(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
             return num3    
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m = maximum(2, 26, 8)
print("value of maxmimum is " +  str(m)) """

""" def printeven(i,N): 
	if(i<=N): 
		print(2*i) 
		printeven(i+1,N) # recursive call 
printeven(1,20) #in place of 10 you can put any number

#programm to print first  50 naturan no
def PrintNaturalNumber(n):
    if(n<=50):
        print(n,end=" ")
        PrintNaturalNumber(n + 1)
n=1
print("First 50 Natural Numbers are:")
PrintNaturalNumber(n)
 """

""" n = 3 #prnt *in n-i times
for i in range (n):
    print("*" * (n-i))
 """

#thisset = ['apple', 'banana', 'mango']
#thisset.remove ('mango')

""" from re import X
def f1():
    x=100
    return X
X = f1() + 1
print(X)  """

#print((3**2)//2)

#for i in range (42) :
   # print ('hi')

#print(3*'7')

#print(("A"+'B')*(1+2))

""" age = 42
age = 24 - 6
print(age) """

""" width = input()
height = input() """
""" area = int(5) * int(4)
print(area//9) """

""" x = 4
x *= 3
print(x) """

""" x = 3
num = 17
print(num % x) """

""" x = 'a'
if(x < 'c'):
    x += 'b'
if(x > 'z'):
    x += 'c'
    
print(x) """

i = 3
while i>=0:
   print(i)
   i = i - 1

