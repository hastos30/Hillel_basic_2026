# numbers = [1, 2, 3, 4, 5, 6]
numbers = [1, 2, 3]
# numbers = [1, 2, 3, 4 ,5]
# numbers = [1]
# numbers = []
print(numbers)

list1 = []
list2 = []

if len(numbers) % 2 != 0:
    list1 = numbers[0: len(numbers) // 2 + 1]
    list2 = numbers[len(list1):]
else:
    list1 = numbers[0:len(numbers) // 2]     
    list2 = numbers[len(list1):]

print(list1)
print(list2)

numbers = [list1, list2]

print(numbers)