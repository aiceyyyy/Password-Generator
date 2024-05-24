import random
import tools

# User Interface
print("Welcome to password generator!")
user_letters_amount = int(input("How many letters do you want your password to have? "))
user_special_characters_amount = int(input("How many special characters do you want your password to have? "))
user_numbers_amount = int(input("How many numbers do you want your password to have? "))
print(" ")

# Random password engine
password_type = []
password = ''

for let in range(0, user_letters_amount):
    password_type.append('letter')

for char in range(0, user_special_characters_amount):
    password_type.append('special_character')

for num in range(0, user_numbers_amount):
    password_type.append('number')

# Shuffle chars types
random.shuffle(password_type)

for element in password_type:

    if element == 'letter':
        random_letter_index = random.randint(0, len(tools.letters) - 1)
        password += tools.letters[random_letter_index]
    elif element == 'special_character':
        random_char_index = random.randint(0, len(tools.special_characters) - 1)
        password += tools.special_characters[random_number_index]
    elif element == 'number':
        random_number_index = random.randint(0, len(tools.numbers) - 1)
        password += tools.numbers[random_number_index]

# Result
print(f"Your password is: {password}")