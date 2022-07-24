from art import logo

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1, n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide,
}

def calculator():
  print(logo)
  num1 = float(input('What is your first number?: '))
  for operation in operations:
    print(operation)
  operation_symbol = input('Pick an operation from the line above: ')
  num2 = float(input('What is your second number?: '))
  calculator_function = operations[operation_symbol]
  final_result = calculator_function(num1,num2)
  print(f'{num1} {operation_symbol} {num2} = {final_result}')

  go_again = input(f"Type 'y' to continue calculating with {final_result} or 'n' to start a new calculation. ")

  while go_again == 'y':
    for operation in operations:
      print(operation)
    new_operator = input('Pick an operation: ')
    new_num = float(input('What is the next number?: '))
    calculator_function = operations[new_operator]
    final_result_2 = calculator_function(final_result, new_num)
    print(f'{final_result} {new_operator} {new_num} = {final_result_2}')
    final_result = final_result_2
    go_again = input(f"Type 'y' to continue calculating with {final_result} or 'n' to start a new calculation. ")

  calculator()
calculator()



  










