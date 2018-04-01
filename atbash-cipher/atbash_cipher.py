from re import sub
from textwrap import wrap

def encode(string):
    return ' '.join(wrap(decode(string), 5))

def decode(string):
    stripped_text = sub('[\s|\W]+', '', string)
    return ''.join([get_inverse_char(c) for c in stripped_text])

def get_inverse_char(char):
    if char.isalpha():
        char = char.lower()
        return chr(2*ord('a')+25-ord(char))
    else:
        return char
