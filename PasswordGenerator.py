import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()"

password = ''

print('Lets make a password! ')
length = int(input('How long should the password be? : '))
question = input('Do you want to choose how many letters, numbers and symbols there should be? (yes/no) : ').lower()

if question == 'yes':
    lettersV2 = int(input('How many letters should there be? : '))
    numbersV2 = int(input('How many numbers should there be? : '))
    symbolsV2 = int(input('And last how many symbols? : '))

    for i in range(lettersV2):
        password += random.choice(letters)

    for i in range(numbersV2):
        password += random.choice(numbers)

    for i in range(symbolsV2):
        password += random.choice(symbols)

    # optional but IMPORTANT (makes password more secure/random looking)
    password = ''.join(random.sample(password, len(password)))

else:
    all_chars = letters + numbers + symbols

    for i in range(length):
        password += random.choice(all_chars)

print(password)