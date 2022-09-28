"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
on = True
while True:
    equation = input("What is the equation: ")
    equation = equation.split(' ')
    if equation[0] == "q":
        break

    if len(equation) < 2:
        print("Not enough input")
    
    else:
        if len(equation) < 3:
            num_1 = equation[1]
            if not num_1.isdigit():
                print("That is not a number")
            else:
                if equation[0] == "square":
                    answer = square(float(equation[1]))
                    print(answer)
                if equation[0] == "cube":
                    answer = cube(float(equation[1]))
                    print(answer)

        else:
            if len(equation) > 2:
                num_1 = equation[1]
                num_2 = equation[2]
                if not num_1.isdigit() or not num_2.isdigit():
                    print("That is not a number")
                else:
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
            
