# numbers = [0, 1, 7, 2, 4, 8]
# numbers = [6]
numbers = []

temp = 0

if len(numbers) != 0:
    for number in numbers[::2]:
        temp += number
        print(number)
    temp *= numbers[-1]
    
print(temp)