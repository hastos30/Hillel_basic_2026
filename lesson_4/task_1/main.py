# numbers = [0, 1, 0, 12, 3]
# numbers = [0]
# numbers = [1, 0, 13, 0, 0, 0, 5]
numbers = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(numbers)

result = []

for number in numbers:
    if number != 0:
        result.append(number)

result += (numbers.count(0) * [0])

print(result)