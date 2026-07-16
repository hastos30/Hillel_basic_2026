print("Калькулятор")

start = True

while start:

    num1 = int(input("\nВведите первое число:"))
    op = input("Введите математическое действие (+, -, *, /)")
    num2 = int(input("Введите второе число:"))

# if op != '-' and op != '+' and op != '*' and op != '/':
#     print("Некорректный символ!")
# else:
#     if op == '+':
#         print("Результат:", num1 + num2)

#     elif op == '-':
#         print("Результат:", num1 - num2)

#     elif op == '*':
#         print("Результат:", num1 * num2)

#     elif op == '/':
#         if num2 != 0:
#             print("Результат:", num1 / num2)
#         else:
#             print("На ноль делить нельзя!")

    match op:
        case '+':
            print("Результат:", num1 + num2)
        case '-':
            print("Результат:", num1 - num2)
        case '*':
            print("Результат:", num1 * num2)
        case '/':
            if num2 != 0:
                print("Результат:", num1 / num2)
            else:
                print("На ноль делить нельзя!")
    
        case _:
            print("Некорректный символ!")

    answer = input("\nХотите продолжить? (yes/no)")
    if answer not in "yes" and answer not in "y":
        start = False
        print("До свидания!")