secret_number = 99
is_secret_number = int(input("Entre the secret number: "))
while secret_number != is_secret_number:
    print("Ha ha! You're stuck in my loop!", is_secret_number)
    is_secret_number = int(input("Try again. Entre the secret number"))
    print("Well done, muggle! You are free now")
       
