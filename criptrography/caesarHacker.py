# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message= input('Enter the message to descript: \n')

#Example this message= guv6Jv6Jz!J6rp5r7Jzr66ntrM 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#loop to every posible key
for key in range(len(SYMBOLS)):
    #we have to blank the string so the previous iteration values is cleared
    translated= ''

    #loop thorugh each symbols in the message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #handle th wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            #append the decrypted symbol
            translated = translated + SYMBOLS[translatedIndex]

        else:
            #append the symbol wothout encryptino/decrypting
            translated = translated + symbol

    #display every posible decryption
    print('key #%s: %s'% (key, translated))