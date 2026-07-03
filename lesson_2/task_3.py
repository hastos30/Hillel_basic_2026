print("Переобразование минут в часы\n")

time = int(input("Введите количество минут: "))

hours = time // 60
minutes = time % 60

print(f"{hours} часов {minutes} минут")
