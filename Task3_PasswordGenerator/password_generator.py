
import random
import string

def generate_password(length):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&()_+-={}:<>?,./"
    
    # Ensure at least one of each type is included in the password
    password_list = [
                    random.choice(uppercase_letters),
                    random.choice(lowercase_letters),
                    random.choice(digits),
                    random.choice(special_chars)
                    ]
    
    # Fill the rest of the password length with random characters from all sets combined
    all_characters_combined = uppercase_letters + lowercase_letters + digits + special_chars
    
    for _ in range(length - 4):
        password_list.append(random.choice(all_characters_combined))
        
    # Shuffle to avoid first four characters always being in the same character type order
    random.shuffle(password_list)
    
    return ''.join(password_list)

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (8-20): "))
            if 8 <= length <= 20:
                break
            else:
                print("Password length must be between 8 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        cont_choice = input("\nGenerate another password? (Y/N): ").upper()
        
        if cont_choice == "Y":
            while True:
                try:
                    length = int(input("Enter the desired new password length (8-20): "))
                    if 8 <= length <= 20:
                        break
                    else:
                        print("Password length must be between 8 and 20.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            break

if __name__ == "__main__":
    main()
