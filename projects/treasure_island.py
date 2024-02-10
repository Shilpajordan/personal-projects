
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("Where path do you want to choose? 'left' or 'right'? ")
if direction == "left":
  print("Great decision! You have arrived the lake")
  decision = input("Do you want to 'swim' or 'wait' for the boat? ")
  if decision == "swim":
    print("You got attacked by trout\nGAME OVER")
  elif decision == "wait":
    print("You have reached the door")
    door = input("Now choose the door 'yellow', 'red' or 'blue'? ")
    if door == 'blue':
      print("You got eaten by beasts\nGAME OVER")
    elif door == "yellow":
      print("Congratulations!!\nYOU WON THE TREASURE")
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    elif door == "red":
      print("You got burnt by fire\nGAME OVER")
    else:
      print("Wrong choice\nGAME OVER!!")
  else:
      print("Wrong choice\nGAME OVER!!")
elif direction == "right":
  print("Oops! you fell into the hole\nGAME OVER")
else:
      print("Wrong choice\nGAME OVER!!")


