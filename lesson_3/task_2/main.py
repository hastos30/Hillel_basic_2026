list1 = [12, 3, 4, 10]
#list1 = [1]
#list1 = []
#list1 = [12, 3, 4, 10, 8]
print(list1)

temp = list1[-1]
list1[-1] = list1[0]
list1[0] = temp

print(list1)