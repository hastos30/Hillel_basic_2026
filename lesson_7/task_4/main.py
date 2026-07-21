def common_elements():
	list1 = [x for x in range(100) if x % 3 == 0]
	list2 = [x for x in range(100) if x % 5 == 0]
	set1 = set(list1)
	set2 = set(list2)
	return set1.intersection(set2)

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("Ok!")