"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
on = True
while True:
    equation = input("What is the equation: ")
    equation = equation.split(' ')
    num_1 = equation[1]
    num_2 = equation[2]

    if len(equation) < 2:
        print("not enough input.")
    
    if num_1.isdigit() == False:
        print("That is not a number, try again")

    if (type(equation[1]) != int) and (type(equation[2]) != int): 
        print("That is not an equation")
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
    if equation[1] != int:
        print("That is not an equation")
    if equation[0] == "square":
        answer = square(float(equation[1]))
        print(answer)
    if equation[0] == "cube":
        answer = cube(float(equation[1]))
        print(answer)
    if equation[0] == "pwr":
        answer = power(float(equation[1]), float(equation[2]))
        print(answer)
    if equation[0] == "mod":
        answer = mod(float(equation[1]), float(equation[2]))
        print(answer)
    if equation[0] == "q":
        print("Exit calculator")
        break
    
