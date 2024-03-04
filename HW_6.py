'''4 FUNCTION'''
"""EVEN - ODD"""
def even_odd (number):
    if number % 2 == 0 and isinstance(number,int):
        print(True)
    elif number % 2 != 0 and isinstance(number,int):
        print(False)
    else:
        print(None)

even_odd(3.9)

"""SPELLING"""
def spelling (word):
    if word == word.capitalize() and word[-1] == ".":
        print(True)
    else:
        print(False)

spelling("War.")

"""CALCULATOR"""
def calculator(number1, operator, number2):
    if operator == '+':
        print(number1 + number2)
    elif operator == '-':
        print(number1 - number2)
    elif operator == '*':
        print(number1 * number2)
    elif operator == '//':
        print(number1 // number2)
    elif operator == '/':
        print(number1 / number2)
    elif operator == '**':
        print(number1 ** number2)
    elif operator == '%':
        print(number1 % number2)
    else:
        print('Enter number please')

calculator(5, '**', 5)

"""NEAREST NUMBER"""
def nearest_number(list, number = 0):
    l = []
    for i in list:
        l.append(abs(number - i))
    minn = min(l)
    ind = l.index(minn)
    print(list[ind])

nearest_number([5, 20.18, 103, 4],27)
nearest_number((312, 996, 31, 1991), 1000)
