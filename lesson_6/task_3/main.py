print("Произведение чисел\n")

numbers = input("Введите целое число: ")

while len(numbers) > 1:
    temp = 1
    for number in numbers:
        temp *= int(number)
    numbers = str(temp)

print(f"Результат: {numbers}")