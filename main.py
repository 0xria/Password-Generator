import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Ask User if they want a generated password
user_input = input("Do you want a password suggestion? (yes/no):").lower()

if user_input == 'yes':
    random_password = generate_password()
    print("Here is your suggested password:", random_password)
elif user_input == 'no':
    print("Alright, no suggested password.")
else:
    print("Invalid input. Please type 'yes' or 'no'.")



