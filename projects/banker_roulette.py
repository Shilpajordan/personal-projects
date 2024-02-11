
import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

# Getting the total number of items in the list
num_items = len(names)
# Generate random numbers between 0 and the last index
random_choice = random.randint(0,(num_items-1))
#Picking a random person
person_buying = names[random_choice]

print(f"{person_buying} is going to buy the meal today!")

