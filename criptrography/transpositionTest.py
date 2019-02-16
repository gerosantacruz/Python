# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys, tranpositionCypher, transpositionDecrypt

def main():
    random.seed(42) 

    print('Starting test....')

    for i in range(20): #run 20 test 
        #generate random messafe 

       message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40) 

       #convert the message strin to a list to shuffle it:
       message = list(message)
       random.shuffle(message)
       message = ''.join(message) #convert the list back to a string

       print('Test #%s: "%s..."' % (i + 1, message[:50]))

       #check all posiles keys for each message
       for key in range(1, int(len(message)/2)):
           encrypted = tranpositionCypher.encript_message(key, message)
           decrypted = transpositionDecrypt.decrypt_message(key, encrypted)

           #if the decryprion doesnt match the original message.
           #display and error and quit
           if message != decrypted:
               print('mismatch key %s and message %s.' % (key, message))
               print('Decrypted as: ' + decrypted)
               sys.exit()

    print('Transposition cipheer test passed')

#call the main() function

if __name__ == '__main__':
    main()