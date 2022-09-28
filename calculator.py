"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
on = True
while True:
    equation = input("What is the equation: ")
    equation = equation.split(',')
    if equation[0] == "+":
        add(float(equation[1]), float(equation[2]))
    if equation[0] == "-":
        subtract(float(equation[1]), float(equation[2]))
    if equation[0] == "*":
        multiply(float(equation[1]), float(equation[2]))
    if equation[0] == "/":
        divide(float(equation[1]), float(equation[2]))
    if equation[0] == "square":
        square(float(equation[1]))
    if equation[0] == "cube":
        cube(float(equation[1]))
    if equation[0] == "pwr":
        power(float(equation[1]), float(equation[2]))
    if equation[0] == "mod":
        mod(float(equation[1]), float(equation[2]))
    if equation[0]:
        on = False