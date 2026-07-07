print("Калькулятор\n")

num1 = int(input("Введите первое число:"))
op = input("Введите математическое действие (+, -, *, /)")
num2 = int(input("Введите второе число:"))

if op != '-' and op != '+' and op != '*' and op != '/':
    print("Некорректный символ!")
else:
    if op == '+':
        print("Результат:", num1 + num2)

    elif op == '-':
        print("Результат:", num1 - num2)

    elif op == '*':
        print("Результат:", num1 * num2)

    elif op == '/':
        if num2 != 0:
            print("Результат:", num1 / num2)
        else:
            print("На ноль делить нельзя!")