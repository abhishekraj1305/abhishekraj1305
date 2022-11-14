""" list = [1,8,5,7,2,3]
list.sort()
#rint (list)
#print(min(list))
list.append(10)
list.insert(0,9)
print(list) """
""" b= ["saw", "rock",  "paper", "sicior", "six"]
b.sort(key=len)
print(b) """

""" empty_dict={}
d1={"a": "some value" , "b":[1,2,3,4]}
"a" in d1
print(d1) """

from typing import Mapping


tuples=zip(range(5), reversed(range(5)))
Mapping=dict(tuples)
print(Mapping)