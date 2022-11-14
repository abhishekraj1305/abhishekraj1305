# create a mapping of state to abbreviation
states = {
    'oregon': 'OR',
    'Florida': 'FL',
    'caifornia': 'CA',
    'New york': 'NY',
    'michigan': 'MI'
}

#create a basics set of states and some cities in them
cities = {
    'CA': 'san fransisco',
    'MI': 'Detroit',
    'FL': 'jacksonville'
}

#add some more cities
cities['NY'] = 'New york'
cities['OR'] = 'portland'

# print out some cities
print('-' * 10)
print("NY state has:", cities['NY'])
print("OR state has:", cities ['OR']) 

# print some state
print('_' * 10)
print("michigan's abbreviation is: ", states ['michigan'])
print("florida's abbreviation is:", states ['Florida'])

#do it by using the states then cities dict
print('-' * 10)
print("michigan has:", cities[states['michigan']])
print("florida has:", cities[states['Florida']])

#print state abbreviation 
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in the state
print('_' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('_'* 10)
for state, abbrev, in list(states.items()):
    print(f"{state} state is abbreviates as a{abbrev}") 
    print(f"and has city {cities[abbrev]}")   

print ("_" *10)
#safely get abbreviation by state that might not be there
state = states.get('Texas') 

if not state:
    print("sorry not texas.")

#get a city with default value 
city = cities.get('TX', 'Does Not Exist')
print (f"the city for the state 'TX' is: {city}")