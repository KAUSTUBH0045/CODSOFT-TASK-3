import secrets
import string
import random
symbols = string.punctuation
alphabets= string.ascii_letters
numbers= string.digits
combination= alphabets + numbers + symbols
charachters=int(input("enter no. charachters for password"))
output= ''
for i in range(0,charachters):
    output+= ''.join(secrets.choice(combination))
print("generated password is:\n",output)
