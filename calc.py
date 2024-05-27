import math

a = input(" >> ")
b = a.split(" ")
b[0], b[2] = float(b[0]), float(b[2])
sign = ['+','-','*','/','^']

if b[1] in sign:
    if b[1] == "+":
        print(b[0] + b[2])
    elif b[1] == "-":
        print(b[0] - b[2])
    elif b[1] == "*":
        print(b[0] * b[2])
    elif b[1] == "/":
        print(b[0] / b[2])
    elif b[1] == "^":
        print(b[0] ** b[2])
