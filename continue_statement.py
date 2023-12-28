user_word = input("Entre a word: ")
user_word = user_word.upper()
vowels = ['A', 'E', 'I', 'O', 'U']
result = ""

for letter in user_word:
    if letter not in vowels:
        result += letter + "\n"

print("Word without vowels:")
print(result)
