import re

def word_count(sentence):
    # split lowered sentence by any non alphanum characters first
    splitSentence = re.split('[\W_]+', sentence.lower())

    # filter out any remaining empty strings
    newSentence = filter(lambda word: word!= "", splitSentence)

    wordDct = {}
    for word in newSentence:
        wordDct[word] = wordDct.get(word, 0) + 1
    return wordDct
