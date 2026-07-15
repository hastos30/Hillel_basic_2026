import random

lenght = random.randint(3, 10)

numbers = []
temp = []

for number in range(lenght):
    numbers.append(random.randint(3, 10))

temp.append(numbers[0])
temp.append(numbers[2])
temp.append(numbers[-2])

print(numbers)
print(temp)