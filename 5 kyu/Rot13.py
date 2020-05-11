'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
'''


def rot13(message):
    cipher = []

    for character in message:
        if character.isalpha():
            if character.islower():
                lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
                i = lowercase_alphabet.index(character)
                count = 0

                while count < 13:
                    # Set i to -1 if index goes out of loop
                    # So it will refer to lowercase_alphabet[0] next (after line 24 executes)
                    if (i == len(lowercase_alphabet)-1):
                        i = -1

                    character = lowercase_alphabet[i+1]
                    count += 1
                    i += 1

            else:  # Must be uppercase
                uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                i = uppercase_alphabet.index(character)
                count = 0

                while count < 13:
                    # Set i to -1 if index goes out of loop
                    # So it will refer to uppercase_alphabet[0] next (after line 39 executes)
                    if (i == len(uppercase_alphabet)-1):
                        i = -1

                    character = uppercase_alphabet[i+1]
                    count += 1
                    i += 1

        cipher.append(character)

    return "".join(cipher)
