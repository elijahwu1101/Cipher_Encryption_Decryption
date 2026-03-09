#Da great machine

def encrypt_ceasar_cipher (text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit(): # Check if the character is a digit
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

def decrypt_ceasar_cipher (text, shift):
    result = ''
    for char in text:
        if char. isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start - shift + 26) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) - shift + 10) % 10)
        else:
            shifted_char = char
        result += shifted_char
    return result

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

def decrypt_vigenere_cipher(text, key_word):
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
            shift = ord(str_key[key_index % keyword_length]) - ord('a')
            # The formula is (Position - Shift)
            result += chr((ord(char) - start - shift + 26) % 26 + start)
            key_index += 1
        else:
            result += char
    return result
            
message = ""
shift_value= 0
    
print("\nThis is a Ceasar Cipher Encrypter/Decrypter")
answer = input ("\nCeasar Cipher or Vigenere Cipher (c/v)? ").lower()
if answer == "v":
    decrypt_encrypt = input("Would you like to encrypt or decrypt in the Vigenere Cipher (e/d): ")
    if decrypt_encrypt == "e":
        message_encrypt = input("\nOk, please type your message you want to encrypt here:")
        key_word = input("\nPlease enter a key word that you would like your message to be encrypted by: ")
        encrypted_message = encrypt_vigenere_cipher(message_encrypt, key_word)
        print("\nEncrypted message:", encrypted_message)

    elif decrypt_encrypt == "d":
        message_decrypt = input("\nOk, please type your message you want to decrypt here:")
        key_word = input("\nPlease enter the key word to decrypt your message: ")
        decrypted_message = decrypt_vigenere_cipher(message_decrypt, key_word)
        print("\nDecrypted message:", decrypted_message)
    else:
        print("_______INVALID_______")

elif answer == "c":
    ceasar_cipher_choice = input("Would you like to encrypt, decrypt, or do an automatic decryption (e/d/a)?")
    if ceasar_cipher_choice == "e":
        message_encrypt = input("\nOk, please type your message you want to encrypt here:")
        shift_value = input("\nPlease enter a shift value for your encrypted message: (An integer)")
        shift_value = int(shift_value)
        encrypted_message = encrypt_ceasar_cipher(message_encrypt, shift_value)
        print("\nEncrypted message:", encrypted_message)

    elif ceasar_cipher_choice == "d":
        message_decrypt = input("\nOk, please type your message you want to decrypt here:")
        shift_value = input("\nPlease enter the shift value you used to encrypt your message: (An integer)")
        shift_value = int(shift_value)
        decrypted_message = decrypt_ceasar_cipher(message_decrypt, shift_value)
        print("\nDecrypted message:", decrypted_message)

    elif ceasar_cipher_choice == "a": 
        message_decrypt = input("\nOk, please type your message you want to decrypt here: ")

        print()
        print("=========================================")

        for shift_try in range(26):
            decrypted_message = decrypt_ceasar_cipher(message_decrypt, shift_try)
            print(f"Shift {shift_try:2}: {decrypted_message}")
    else:
        print("_______INVALID_______")
