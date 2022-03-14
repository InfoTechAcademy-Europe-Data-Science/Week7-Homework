"""Question 2:
Find words that are 8 letter long on this text ;

Without, the night was cold and wet, but in the small parlour of Laburnum villa the blinds were drawn and the fire burned brightly. Father and son were at chess; the former, who possessed ideas about the game involving radical chances, putting his king into such sharp and unnecessary perils that it even provoked comment from the white-haired old lady knitting placidly by the fire. "Hark at the wind," said Mr. White, "who, having seen a fatal mistake after it was too late, was amiably desirous of preventing his son from seeing it. I'm listening," said the latter grimly surveying the board as he stretched out his hand. "Check." I should hardly think that he's come tonight," said his father, with his hand poised over the board. "Mate," replied the son. "That's the worst of living so far out," balled Mr. White with sudden and unlooked-for violence; "Of all the beastly, slushy, out of the way places to live in, this is the worst. Path's a bog, and the road's a torrent. I don't know what people are thinking about. I suppose because only two houses in the road are let, they think it doesn't matter." """

import os
import re
def create_txt():
    path="text.txt"
    print()
    with open(path,'w', encoding = 'utf-8') as f:
        f.write("")
print(os.getcwd())
#create_txt()

def read_my_txt():
    f=open("text.txt","r")
    lines=f.readlines()
    #print(len(lines[0])) #1109 letters
    words=re.split("\s|(?<!\d)[,.](?!\d)",lines[0]) 
    #print(len(words)) #196 words  
    for word in words:
        if len(word)==8:print(word)      
read_my_txt()    


