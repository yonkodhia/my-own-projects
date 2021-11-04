#code by cherni dhia 
import random as rand
chars ="abcdefghijklmnopqrstuvwxyz" # alphab min
CHARS = chars.upper()   # alphab maj
symbols = "[]{}()*;/,._-" # les symbols
numbers = "0123456789" # numbers

allVariables = chars + CHARS + symbols + numbers 
len = 16 

passwords = "".join(rand.sample(allVariables , len))
print(passwords)
#enjoy your security
