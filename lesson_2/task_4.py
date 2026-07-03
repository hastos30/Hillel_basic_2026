print("Расчет скидки\n")

input_price = int(input("Введите цену: "))
input_discount = int(input("Введите скидку (%): "))

discount = input_price * input_discount / 100
result = input_price - discount

print(f"Цена со скидкой: {result}")