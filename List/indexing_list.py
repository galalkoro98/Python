numbers = [10, 5, 7, 22, 10]
print("the number are: ", numbers)

numbers[0] = 111
print("after change the first element to 111: ", numbers)

numbers[1] = numbers[4]
print("new list contains: ", numbers)
print("the firs element in the list:", numbers[0])
print("the value of the:", len(numbers))

del numbers[1]
print("the length of numbers: ", len(numbers))
print("After delete second element: ", numbers)
numbers[4] = 35
print("the value that can not be access which does not exist:", numbers[-4])



