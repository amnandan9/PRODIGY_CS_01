# Caesar Cipher Program

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters as is
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # Decrypt by reversing the shift

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").upper()
        if choice == 'E':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            print(f"Encrypted Message: {encrypt(text, shift)}")
        elif choice == 'D':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-25): "))
            print(f"Decrypted Message: {decrypt(text, shift)}")
        elif choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()
