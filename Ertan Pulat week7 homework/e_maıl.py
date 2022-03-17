""" 
Question 3:
Write a program that list according to email addresses without email domains in a text.
Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
Then New Yorker article on wind farms...
Output :
franky
sinatra123
"""
import re 
mail_example = input("Please enter a sample e-mail:") 
patern = r"\b\w+@"                
for eslesme in re.finditer(patern,mail_example):
    print(eslesme.group().split("@"))