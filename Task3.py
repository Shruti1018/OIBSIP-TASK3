import string
import random

def get_password_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Password length must be a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_character_set():
    character_sets = {
        '1': string.ascii_letters,
        '2': string.digits,
        '3': string.punctuation
    }
    
    selected_sets = []
    
    print("Select character sets to include in the password:")
    print("1: Letters (a-z, A-Z)")
    print("2: Numbers (0-9)")
    print("3: Symbols (!, @, #, etc.)")
    
    while not selected_sets:
        choices = input("Enter your choices (e.g., 123 for all): ")
        for choice in choices:
            if choice in character_sets:
                selected_sets.append(character_sets[choice])
            else:
                print(f"Invalid choice: {choice}. Please select 1, 2, and/or 3.")
                selected_sets = []
                break
    
    return ''.join(selected_sets)

def generate_password(length, char_set):
    return ''.join(random.choice(char_set) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")
    length = get_password_length()
    char_set = get_character_set()
    password = generate_password(length, char_set)
    print(f"Generated New Password: {password}")

if __name__ == "__main__":
    main()
