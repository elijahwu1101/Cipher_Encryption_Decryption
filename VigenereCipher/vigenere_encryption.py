
def encrypt_vigenere_cipher(text, key_word):
    result = ''
    if not key_word.isalpha():
        print("Your keyword must only contain letters!")
        return text
    
    str_key = key_word.lower() # Use this for consistent math
    keyword_length = len(str_key)
    key_index = 0

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Always subtract ord('a') because str_key is lowercase
            shift = ord(str_key[key_index % keyword_length]) - ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
            key_index += 1
        else:
            result += char
    return result
