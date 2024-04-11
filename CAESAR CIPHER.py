def caesar_cipher(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Don't change other characters (like spaces or punctuation)
        else:
            result += char

    return result

# Example usage:
text = "Hello, World!"
shift = 3

encrypted = caesar_cipher(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = caesar_cipher(encrypted, -shift)
print(f"Decrypted: {decrypted}")