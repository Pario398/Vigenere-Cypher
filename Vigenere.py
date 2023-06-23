def encrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            shifted_char = ord(char) + shift
            if char.islower():
                result += chr((shifted_char - 97) % 26 + 97)
            else:
                result += chr((shifted_char - 65) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index].upper()) - 65
            shifted_char = ord(char) - shift
            if char.islower():
                result += chr((shifted_char - 97) % 26 + 97)
            else:
                result += chr((shifted_char - 65) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

mode = input("Do you want to encrypt or decrypt? ")
key = input("Enter the key: ")
text = input("Enter the text: ")

if mode == "encrypt":
    result = encrypt(text, key)
elif mode == "decrypt":
    result = decrypt(text, key)

filename = input("Enter the name of the output file: ")
with open(filename, "w") as f:
    f.write(result)
