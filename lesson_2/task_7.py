print("Выведение числа в столбик\n")

number = int(input("Введите 4-х значное целое число: "))

num1 = number // 1000
num2 = (number - (num1 * 1000)) // 100
num3 = ((number - (num1 * 1000)) - num2 * 100) // 10
num4 = ((number - (num1 * 1000)) - num2 * 100) % 10

"""
Можно сократить код:
num1 = number // 1000
num2 = number % 1000 // 100
num3 = number % 100 // 10
num4 = number % 10
"""

print(num1)
print(num2)
print(num3)
print(num4)
