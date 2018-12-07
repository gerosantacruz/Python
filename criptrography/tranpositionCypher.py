# Transposition Cipher Encryption
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    message = input('Insert the message to encrypt: \n')
    key= int(input('Insert the key please: \n'))

    ciphertext = encript_message(key, message)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
     #  the end of the encrypted message:
    print(ciphertext + '|')

    #copy the encrypted string in ciphertext to the clipboard
    pyperclip.copy(ciphertext)

def encript_message(key, message):
    #each string in ciphertext represents a column in the grid
    ciphertext = [''] * key

    #loop through each column in ciphertext
    for column in range(key):
        currentIndex = column

        #keep lopping unitl currentIndex goes past the lenght message
        while currentIndex < len(message):
            #place the carracter at currentIndex in message at the eend of the current 
            #column in the ciphertext list:
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return ''.join(ciphertext)

#if tranpositioncipher is run call the main function

if __name__ == '__main__':
    main()

