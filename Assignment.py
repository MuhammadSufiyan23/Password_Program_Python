
# PASSWORD PROGRAM

min_password_length = 7
max_password_length = 15

user_input = input("Enter Your Password: ")

if min_password_length <= len(user_input) <= max_password_length:
    print("Correct Password!")
else:
    print("Password length should be between 7 and 15 characters.")
