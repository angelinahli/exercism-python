from re import split

def abbreviate(name):
    name_words = split('[\s|-]+', name)
    return ''.join(wd[0].upper() for wd in name_words)
