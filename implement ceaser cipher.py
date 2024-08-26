def caesar_cipher(text, shift, operation):
    result = ""

    # Adjust the shift for decryption
    if operation == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Perform the shift
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep non-alphabet characters unchanged
            result += char

    return result

def main():
    # Get user input
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    operation = input("Do you want to encrypt or decrypt? ").lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
        return

    # Perform the operation
    result = caesar_cipher(message, shift, operation)
    print(f"The {operation}ed message is: {result}")

if __name__ == "__main__":
    main()
