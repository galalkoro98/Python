# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
# write a line of code that removes the last element from the list (Step 2)
# write a line of code that prints the length of the existing list (Step 3).

hat_list = [1, 2, 3, 4, 5]

user_input = int(input("Entre an integer number: "))
hat_list[2] = user_input
del hat_list[-1]
print(len(hat_list))
print(hat_list)