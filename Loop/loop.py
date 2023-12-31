# print("The break instruction:")

# for i in range(1, 6):
#     if i == 3:
#         break
#     print("inside the loop", i)
# print("outside of the loop")

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("skip this iteration", i)
#     print("outside of the loop")
# number = int(input("Entre number: "))

# for number in range(5):
#         print(number)
    
while True:
    word = input("Enter a word: ")
    if word.lower() == "chupacabra":
        print("You've successfully left the loop.")
        break

    