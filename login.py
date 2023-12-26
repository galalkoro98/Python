# Dictionary to store usernames and passwords
user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists and passwords match
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password")

# Call the login function
login()
