def Caesar(word, shift):
    encoded = ""
    for char in word:
        encoded += chr(((ord(char.lower()) - 97 + shift) % 26) + 97)
    return encoded.upper() if word.isupper() else encoded

def Vigenere(word, key):
    key = (key * ((len(word) // len(key)) + 1))[:len(word)]
    encoded_word = ""
    for i, char in enumerate(word):
        key_char = key[i]
        encoded_char = chr(((ord(char) - 65 + ord(key_char) - 65) % 26) + 65)
        encoded_word += encoded_char
    return encoded_word

# Tests
print("Caesar('HELLO', 3) =>", Caesar("HELLO", 3))  # EBIIL selon ton code, mais en vrai ce serait KHOOR
print("Vigenere('HELLO', 'THREE') =>", Vigenere("HELLO", "THREE"))  # ALCPS
