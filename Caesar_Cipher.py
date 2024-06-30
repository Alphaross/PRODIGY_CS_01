def caesar_cipher(text, shift, decrypt=False):
    result = ""
   # Adjust the shift for decryption
    if decrypt:
        shift = -shift
   # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value depending on whether the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet using modulo operation
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # If it's not an alphabetical character, just append it as is
            result += char

    return result

def main():
    # This is user input
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    operation = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if operation == 'e':
        encrypted_message = caesar_cipher(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif operation == 'd':
        decrypted_message = caesar_cipher(message, shift, decrypt=True)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid operation. Please type 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
