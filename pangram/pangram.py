def is_pangram(word):
    word = filter(lambda char: char.isalpha(), word)
    return len(set(list(word.lower()))) == 26