def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # If we are decoding, we can just invert the shift 
    # and reuse the exact same mathematical logic.
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        # Check for uppercase letters
        if char.isupper():
            start = ord('A')
            # Shift, wrap around the 26-letter alphabet using modulo, then convert back to a char
            result += chr((ord(char) - start + shift) % 26 + start)
            
        # Check for lowercase letters
        elif char.islower():
            start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            
        # Leave punctuation, spaces, and numbers completely untouched
        else:
            result += char
            
    return result


def main():
    print("==============================")
    print("    CAESAR CIPHER PROGRAM     ")
    print("==============================\n")
    
    # --- Step 1: Get valid operation mode ---
    while True:
        mode_input = input("Would you like to (E)ncrypt or (D)ecrypt? ").strip().upper()
        
        if mode_input in ['E', 'ENCRYPT']:
            mode = 'encrypt'
            break
        elif mode_input in ['D', 'DECRYPT']:
            mode = 'decrypt'
            break
            
        print("Oops, invalid choice. Please enter 'E' or 'D'.\n")

    # --- Step 2: Get the message from the user ---
    while True: 
        user_text = input("Enter your message: ").strip()
        
        if not user_text:
            print("The message cannot be empty. Try again.")
        else:
            break

    # --- Step 3: Get and validate the numeric key ---
    while True:
        try:
            shift_key = int(input("Enter the shift key (a whole number): "))
            break
        except ValueError:
            print("That's not a valid number. Please enter an integer (e.g., 3, -5, 12).\n")

    # --- Step 4: Process and output the results ---
    processed_text = caesar_cipher(user_text, shift_key, mode)
    
    print("\n------------------------------")
    print(f"Result ({mode}ed): {processed_text}")
    print("------------------------------")


if __name__ == "__main__":
    main()