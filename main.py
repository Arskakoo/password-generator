import random

def generate_letter():
    letters = "abcdefghijklmnopqrstuvwxyz"
    return random.choice(letters)

def generate_number():
    numbers = "1234567890"
    return random.choice(numbers)

def generate_special_character():
    special = ":;_-<>,.´¨'`^*!#€%&/()="
    return random.choice(special)

def generate_password(length, include_letters=True, include_numbers=True, include_special=True):
    possible_characters = ""

    if include_letters:
        possible_characters += "abcdefghijklmnopqrstuvwxyz"
    if include_numbers:
        possible_characters += "1234567890"
    if include_special:
        possible_characters += ":;_-<>,.´¨'`^*!#€%&/()="

    if not possible_characters:
        print("Error: No character types selected.")
        return None

    password = [random.choice(possible_characters) for _ in range(length)]
    return "".join(password)

# Ask user for preferences
print("""    ____                                          __
   / __ \____ ____________      ______  _________/ /
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
/_/    \__,_/____/____/ |__/|__/\______/   \__,_/   
   ____ ____  ____  ___  _________ _/ /_____  _____ 
  / __ `/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/ 
 / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /     
 \__, /\___/_/ /_/\___/_/   \__,_/\__/\____/_/      
/____/                                              """)
print("")
include_letters = input("Include letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# Ask user for total number of characters
total_chars = int(input("Enter the total number of characters for the password: "))

# Generate and print password
password = generate_password(total_chars, include_letters, include_numbers, include_special)

if password:
    print("Generated password: ", password)
