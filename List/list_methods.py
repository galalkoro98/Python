# list = [1, 2, 3, 4, 5, 6]

# list.append("hi")
# print(f"Original List: {list}")

# list.clear()
# print(f"\nCleared List: {list}\n")

# list.copy()
# print(f"\nList Copy: {list.copy()}\n")

# my_list = []

# for i in range(5):
#     my_list.insert(0, i + 1)

# print(my_list)


# my_list = [10, 1, 8, 3, 5]
# total = 0

# # for i in range(len(my_list)):
# #     total = total + my_list[i]

# for i in my_list:
#     total = total + i

# print(f"The sum of the values is: {total}")

my_list = [10, 1, 8, 3, 5]
length = len(my_list)

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


