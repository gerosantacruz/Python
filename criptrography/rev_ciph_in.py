#Reverse cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = input('Put the message to be coding: \n')
translated=''

i=len(message) -1
while i>= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
