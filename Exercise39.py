#Dictionaries, Oh Lovely Dictionaries!

# create mapping of states to abbrieviation

states = {'Oregon':'OR', 'Florida':'FL', 'California':'CA','New York':'NY','Michigan':'MI'}

# create basic set of states and some cities in them 

cities = {'CA':'San Francisco', 'MI':'Detroit','FL':'Jacksonville'}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Oregon'

# add some more cities

print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# print some states

print('-' * 10)
print("Michigan's abbrieviation is: ", states['Michigan'])
print("Florida's abbrieviation is: ", states['Florida'])

# do it by using the state then cities dict

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbrieviation 

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbrieviated {abbrev}")

# print every city in the state

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev} and has city {cities[abbrev]}")

print('-' * 10)

# safely get an abbriviation of a state which might not be there

state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")