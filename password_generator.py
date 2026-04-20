# Mon 20 Apr, 9;26 pm

import random
import string


def generate_characters(min_length, has_number = True, has_special = True):
    # Initialize variable with "string" imported
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    # Characters would first contain letters imported via "string" package (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ)
    characters = letters
    if has_number:
        # Numbers would be added inside characters variable imported via "string" package (0123456789)
        characters += numbers≈
    if has_special:
        # Special characters would be added inside characters variable imported via "string" package (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
        characters += special

    # Sections to make the randomized password followed the criteria
    pwd = "" 
    criteria = False
    number_added = False
    special_added = False

    while not criteria or len(pwd) < min_length: # always run for the first time
        new_characters = random.choice(characters) # added random character by using "random" package
        pwd += new_characters # keep adding new characters to the "pwd" 

        # Sections to basically verify all criteria is checked 
        if new_characters in numbers:
            number_added = True
        elif new_characters in special:
            special_added = True

        criteria = True
        if has_number:
            criteria = number_added
        if has_special:
            criteria = criteria and special_added

    return pwd 

# Input from users
min_length = int(input("Enter minimum length: "))
has_number = input("Do you want number? (y/n): ").lower() == "y"
has_special = input("Do you want symbol? (y/n): ").lower() == "y"
pwd = generate_characters(min_length, has_number, has_special)
print (pwd)
