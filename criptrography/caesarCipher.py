""" Ceaser cipher
https://www.nostarch.com/crackingcodes/ (BSD Licensed)
"""

import pyperclip

#Whether the program encrypts or decrypts.
mode= input("encrypt or decrypt: \n").lower() #set eithrt to encrypt or decrypt

#The string to be encrypted/decypted:
message= input("Write your secret Message: \n")

key = int(input('Insert the key please: \n'))



#every posible symbol cona be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#Store the encrypted/decrypted form of the message
translated = ""

for symbol in message:
    #only symbols in SYMBOLS van be encrypted
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)

        #perfom encryption or decryption
        if mode == 'encrypt':
            translated_index= symbol_index + key 
        elif mode == 'decrypt':
            translated_index = symbol_index - key 
        
        #handle wraparoun if needed.
        if translated_index >= len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)

        translated= translated + SYMBOLS[translated_index]

    else:
        #append the symbol withouth encrypting
        translated = translated + symbol
#output the translated string
print(translated)
pyperclip.copy(translated)   