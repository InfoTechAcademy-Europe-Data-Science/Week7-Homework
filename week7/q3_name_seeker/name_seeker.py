"""Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

Output :

franky

sinatra123"""

import os
import re

print(os.getcwd())

def txt_creator():
    path="text.txt"
    with open(path,'w', encoding = 'utf-8') as f:
        f.write("The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...")

txt_creator()

def export_name():
    f=open("text.txt","r")
    words=re.split(' ',f.read())
    for i in words:
        if len(re.findall('@',i)) != 0:
            name=i.split('@')
            print(name[0])

export_name()    