def is_isogram(word):
    word = filter(lambda char: char.isalpha(), word)
    return len(word.lower()) == len(set(list(word.lower())))