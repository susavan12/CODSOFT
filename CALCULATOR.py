import os
def add(a,b):
 return a+b
def subtract(a,b):
 return a-b
def multiply(a,b):
 return a*b
def divide(a,b):
 return a/b
operations_dict={
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}
def calculator():
    number1=float(input("Enter first number: "))
    for symbol in operations_dict:
     print(symbol)
    continue_flag=True
    while continue_flag:
        op_symbol=input("Pick an operation: ") #+
        number2=float(input("Enter next number: "))
        calulator_function=operations_dict [op_symbol] #add
        output=calulator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue=input(f"Enter 'a' to continue calculation with {output} or 'd' to start a new calculator or 'x' to exit: ").lower()
        if should_continue=='a'or should_continue=='A':
           number1=output
        elif should_continue=='d' or should_continue=='D':
          continue_flag=False
          os.system('cls')
          calculator()
        elif should_continue=='x' or should_continue=='X':
          continue_flag=False
          print("Calculator CLOSE!")
        else :
          continue_flag=False
          print("!!Syntax Error!!")
calculator()