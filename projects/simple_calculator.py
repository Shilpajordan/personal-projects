import os
def clear():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
# Add
def add(n1 , n2):
  return n1 + n2

# Subtract
def subtract(n1 , n2):
  return n1 - n2

# Multiply
def multiply(n1 , n2):
  return n1 * n2

# Divide
def divide(n1 , n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}

def calculation():
    print(logo)
    num_1 = int(input("Enter the first number: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while  should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num_2 = int(input("Enter the second number: "))
        calculation_function= operations[operation_symbol]
        answer = calculation_function(num_1,num_2)

        print(f"{num_1} {operation_symbol} {num_2} = {answer}")
        recalc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation and 'x' to exit.: " )

        if recalc =='y':
                num_1 = answer
        elif recalc == 'n':
            should_continue = False
            clear()
            calculation()
        elif recalc == 'x':
            should_continue = False


calculation()