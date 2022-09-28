"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
on = True
while True:
    equation = input("What is the equation: ")
    equation = equation.split(' ')
    OPERATORS = ["+", "-", "*", "/", "square", "cube", "pwr", "mod"]
    SHORT_OPERATORS = ["squre", "cube"]
    #first character input is "q", quit calculator
    if equation[0] == "q":
        break
    #first input character input does not match requirement
    if equation[0] not in OPERATORS:
        print("Not an operator")
    else:

        if len(equation) < 2:
            print("Not enough input")
        
        else:
            if len(equation) < 3:
                num_1 = equation[1]
                if equation[0] not in SHORT_OPERATORS:  #check if correct operators
                    print("Not enough input")
                if not num_1.isdigit():             #check if input are digits
                    print("That is not a number")
                else:
                    ## 1 digit function (square and cube)

                    if equation[0] == "square":
                        answer = square(float(equation[1]))
                        print(answer)
                    if equation[0] == "cube":
                        answer = cube(float(equation[1]))
                        print(answer)

            else:
                num_1 = equation[1]
                num_2 = equation[2]
                if not num_1.isdigit() or not num_2.isdigit():  #check if input are digits
                    print("That is not a number")  
                else:
                    ## 2 digit calculation (+, -, *, /,...)
                    
                    if equation[0] == "+":
                        answer = add(float(equation[1]), float(equation[2]))
                        print(answer)
                    if equation[0] == "-":
                        answer = subtract(float(equation[1]), float(equation[2]))
                        print(answer)
                    if equation[0] == "*":
                        answer = multiply(float(equation[1]), float(equation[2]))
                        print(answer)
                    if equation[0] == "/":
                        answer = divide(float(equation[1]), float(equation[2]))
                        print(answer)
                    if equation[0] == "pwr":
                        answer = power(float(equation[1]), float(equation[2]))
                        print(answer)
                    if equation[0] == "mod":
                        answer = mod(float(equation[1]), float(equation[2]))
                        print(answer)
            
