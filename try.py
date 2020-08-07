'''
author: Zeyu
date: 07-08-2020
operte: learning pandas
'''

input_str = 'The weather is good today, very good!'
input_str.strip() #strip function could be used for deleting the blank space..
input_str.rstrip()#right delete
input_str.lstrip()#left delete


input_str.strip('A') #delete the words 'A' at the start and the end of this sentence
input_str.replace('The','that')# replace 'The' with 'that'
input_str.replace('The','')#remove 'The' which is special character

## find operation
input_str.find('very')
## judgement operation
input_str = 'ABC'
a = input_str.isalpha()#generate if all of them are alpha
b = input_str.isdigit()#generate if all of them are digitials
print(a,b)

## cut and concate
input_str = 'The weather is good today, very good!'
input_str = input_str.split(' ')# creat a list devise by ' ' blank space
print(input_str)
a = ' '.join(input_str)# combine these words together
print(a)

help(str)## get help from the official word
