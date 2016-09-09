import os
import random
import sys
    
#PROMPT 1
print("Enter filename:")
filename = input('--> ')

# READING AND DISPLAYING ORIGINAL FILE
try:
    test_file = open(filename,'r+')
except IOError:
    print('There was an error opening the file!')
    sys.exit()
    
print("Original text: \n")
text = str(test_file.read())
print(text)

#PROMPT 2 
print('Enter password to encrypt/decrypt')
password = input('--> ')
a = "123"
if(password != a):
    print('Wrong password')
    sys.exit()
    
#PROMPT 3
print('To encrypt press 1 / to decrypt press 0')
button = input('--> ')
button = int(button)
if(button !=0 and button !=1):
    print('Error')
    sys.exit()

#INITIALIZING LISTS AND DICTIONARIES 
char_arr = list(text)
#create a dictionary for this part replacing 1 letter with another
alphabet = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r','s',
            't','u','v','w','x','y','z']

#Original Dictionary
mydict = {}
x=0
for let in alphabet:
    mydict[x]=let
    x=x+1

#Modified Dictionary
mydict2 = {}
x=25
for let in alphabet:
    mydict2[x] = let
    x=x-1

# Replace letters with corresponding number value from dictionary
if(button == 1):
    for x in range(len(char_arr)):
        for y in range(26):
            if(char_arr[x] == mydict[y]):
                char_arr[x] = y

if(button == 0):
    for x in range(len(char_arr)):
        for y in range(26):
            if(char_arr[x] == mydict2[y]):
                char_arr[x] = y

#To encrypt replace numbers with corresponding value from modified dictionary
if(button == 1):
    for x in range(len(char_arr)):
        for y in range(26):
            if(char_arr[x] == y):
                char_arr[x] = mydict2[y]

#To decrypt replace numbers with mydict values
if(button == 0):
    for x in range(len(char_arr)):
        for y in range(26):
            if(char_arr[x] == y):
                char_arr[x] = mydict[y]

# PRINTING RESULT 
print("New text:\n")
newText = ''.join(char_arr)
print(newText)
test_file.close()

print("Enter output filename:")
outfilename = input('--> ')
out_file = open(outfilename,'w')
out_file.write(newText)

out_file.close()



