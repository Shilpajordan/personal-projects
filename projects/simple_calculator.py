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

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

for operation in operations:
  print(operation)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function= operations[operation_symbol]
first_answer = calculation_function(num_1,num_2)

print(f"{num_1} {operation_symbol} {num_2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num_3 = int(input("Enter the next number: "))
calculation_function= operations[operation_symbol]
second_answer = calculation_function(first_answer, num_3)

print(f"{first_answer} {operation_symbol} {num_3} = {second_answer}")