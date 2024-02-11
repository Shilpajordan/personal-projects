'''write a program that will mark a spot on a map with an X.'''

line1 = ["⬜️","️⬜️","️⬜️"]
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input('Where do you want to put the tressure? ')

# Getting the first letter of the input
letter = position[0].lower()
#print(letter)
# Turn the letter to lower case to compare it with a comparable
abc = ['a','b','c']
letter_index = abc.index(letter)# getting the index position of the index in comparison with the abc
#print(letter_index)

#Getting the index position of the number of the letter ex:B3 so here '3'
number_index = int(position[1])-1# -- since index starts from 0 in a list

# Making changes in the map list to replace the value to X
map[number_index][letter_index] = "X" # map is a nested list
                                      # here number index is the first index  

print(f"{line1}\n{line2}\n{line3}")