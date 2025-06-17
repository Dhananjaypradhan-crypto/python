letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)
def encrypt(planetext, key):
    ciphertext = ''
    for char in planetext:
        letter=letter.lower()
        if not letter== ' ':
            index=letters.find(letter)
            if index== -1:
                ciphertext += letter
            else:
                new_index = index+key
                if new_index >= 26:
                    new_index -= 26
                ciphertext += letters[new_index]
                return ciphertext
def decrypt(ciphertext, key):
    planetext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                planetext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                planetext += letters[new_index]
                return planetext
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'e':
        key= -key
        for letter in text:
            letter = letter.lower()
            if not letter == ' ':
                index = letters.find(letter)
                if index == -1:
                    result += letter
                else:
                    new_index = index + key
                    if new_index >= num_letters:
                        new_index -= num_letters
                    elif new_index < 0:
                        new_index += num_letters
                    result+= letters[new_index]
                    return result 
print()
print('***CAESAR CIPHER ENCRYPTION AND DECRYPTION***')
print()
print('do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()
print()
if user_input == 'e':
    print('You chose to encrypt.')            
    print()
    key=int(input('Enter the key (1-25): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = encrypt_decrypt(text,user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1-25): '))
    text = input('Enter the text to decrypt: ')
    planetext = encrypt_decrypt(text,user_input, key)
    print(f'PLAINTEXT: {planetext}')
    