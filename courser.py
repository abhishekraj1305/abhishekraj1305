""" course = {'1': 'CIT590',
          '2': 'CIT591',
          '3': 'CIT593'}
print(course['1'])  """

""" d = {'A': 1, 'B': 2, 'C': 3}
list(d.keys()) """


""" new_dict = {"A" : "Apple", "B" : "Ball", "C" : "Cat"}
keys = new_dict.keys()

for k in keys:
  print(k, ':', new_dict[k], end = ', ') """
  
""" with open("text.txt", "r") as f:
    lines = f.readlines() """

""" new_dict = {"A" : "Apple", "B" : "Ball", "C" : "Cat"}
keys = new_dict.keys()

for k in keys:
  print(k, ':', new_dict[k], end = ', ')  """  


for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)