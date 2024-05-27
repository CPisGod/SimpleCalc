a = input("수를 입력하세요 ( 예 : 6 + 8 ) > ")
b = a.split(" ")
b[0], b[2] = float(b[0]), float(b[2])
sign = ['+','-','*','/','^']

if b[1] in sign:
    if b[1] == "+":
        print(f'결과 : {b[0]} + {b[2]} = {b[0] + b[2]}')
    elif b[1] == "-":
        print(f'결과 : {b[0]} - {b[2]} = {b[0] - b[2]}')
    elif b[1] == "*":
        print(f'결과 : {b[0]} * {b[2]} = {b[0] * b[2]}')
    elif b[1] == "/":
        print(f'결과 : {b[0]} / {b[2]} = {b[0] / b[2]}')
    elif b[1] == "^":
        print(f'결과 : {b[0]} ^ {b[2]} = {b[0] ** b[2]}')
