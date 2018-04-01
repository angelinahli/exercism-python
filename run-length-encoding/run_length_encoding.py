from re import findall

def decode(message):
    newMessage = findall(r'\d*.', message)
    returnMessage = []

    for char in newMessage:
        char = list(char)
        newChar = char[-1]

        try:
            newNum = int(''.join(char[:-1]))
        except ValueError:
            newNum = 1

        returnMessage.append(newNum*newChar)
    return ''.join(returnMessage)

def encode(message):
    """newMessage structured as list of lists [# occurence, letter]"""
    newMessage = []

    for char in message:
        # if empty list or different char, add a new list
        if not newMessage or newMessage[-1][1] != char:
            newMessage.append([0, char])
        # increase charCount by one
        newMessage[-1][0] += 1

    newMessage = map(encodeLst, newMessage)
    return ''.join(newMessage)

def encodeLst(charLst):
    num, char = charLst
    if num == 1:
        return char
    return str(num) + char