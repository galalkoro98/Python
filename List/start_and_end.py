# my_list = [10, 8, 6, 4, 2]
# # new_list = my_list[1: -1]
# # print("the result", new_list)

# del my_list[1:3]
# print(my_list)

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if largest < my_list[i]:
#         largest = my_list[i]

# print("the result are", largest)


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

