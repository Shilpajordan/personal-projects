
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


