
import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

num_items = len(names)
random_choice = random.randint(0,(num_items-1))
person_buying = names[random_choice]

print(f"{person_buying} is going to buy the meal today!")

