x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)


# blocks = int(input("Entre your blocks number: "))
# height = 0
# needed_block = True
# while needed_block:
#     blocks = blocks - (1 + height)
#     if blocks < 0:
#         break
#     else:
#         height = height + 1
#         print("The height of the pyramid is", height)