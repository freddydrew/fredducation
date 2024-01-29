import re #for regexp
from unidecode import unidecode #transliterate spanish 

'''
This function will take the provided string and make it ready to 
be used as a slug. A slug will be used in the unique URL for a given 
post on this site and cannot contain non-Ascii characters or spaces. 
'''

def slugfiy(str):
    #to lower case, lose trailing/leading whitespace
    str = str.lower().strip() 
    str = unidecode(str) #replace spanish chars with ascii
    #checks regexp patterns and replaces chars with spaces and dash
    str = re.sub(r'[^\w\s-]', '', str)
    str = re.sub(r'[\s_-]+', '-', str)
    str = re.sub(r'^-+|-+$', '', str)
    return str

