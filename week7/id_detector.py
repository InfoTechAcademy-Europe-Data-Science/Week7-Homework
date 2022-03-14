# REGEX Regular Expressions (Regex)
"""Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6"""

import re
def get_str():
    get_text=input("Enter a string: ")
    return get_text
def detect_id(get_text):
    matches=re.findall('[A-Za-z][A-Za-z][0-9][A-Za-z][A-Za-z][0-9][0-9][A-Za-z][0-9]',get_text )
    print(*matches)

x=get_str()
detect_id(x)
