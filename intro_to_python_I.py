import random

#Create a list of random numbers between -25 and 25

random_list = []

for i in range(1, 11):
    x = random.randint(-25, 25)
    random_list.append(x)

#print(random_list)

#Using the previous list, use a list comprehension to create a new list that only contains negative numbers

negatives = [n for n in random_list if n < 0]

#print (negatives)

#Create a tuples with 3 of your favorite foods, loop through the tuple and print out each item

favoritefoods = ("pizz", "pasta", "steak")
for var in favoritefoods:
    print (var)

#Create a set of 10 random numbers between 1 and 100, search the set for the value 50 then print out a statement indicating whether or not the set contains 50

