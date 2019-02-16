 # Transposition Cipher Decryption
 # https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import math, pyperclip

def main():
    message = input('Enter the message to decrypt \n')
    key = int(input('Please enter the key: \n'))

    plain_text = decrypt_message(key, message)

    print(plain_text + '|')


def decrypt_message(key, message):

    #the numbers of columns in our transposition grid:
    num_of_columns = int(math.ceil(len(message)/float(key)))

    num_of_rows = key

    #the number of shaded boxes in the last column of the grid:
    num_shades_boxes = (num_of_columns * num_of_rows) - len(message)

    #each strin in the plaintext represents a column in the grid:
    plain_text = [''] * num_of_columns

    #the column and row variables point to where in the grid the next
    #character in the encrypted message will go
    column = 0
    row = 0

    for symbol in message:
        plain_text[column] += symbol
        column += 1 #point to the next column

        #if there are no more columns or we are at shade box
        #go back to the first column and the next row
        if(column == num_of_columns) or (column == num_of_columns -1 and
        row >= num_of_rows - num_shades_boxes):
            column = 0
            row += 1
    return ''.join(plain_text)

""" if decrypt is run(inste of imported as module)
call the main function """

if __name__ == '__main__':
    main()



