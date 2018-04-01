from re import sub

def hey(message):
    # strips of all whitespace chars
    newMessage = message.strip()

    if not newMessage:
        return 'Fine. Be that way!'
    elif newMessage.isupper():
        return 'Whoa, chill out!'
    elif newMessage.endswith('?'):
        return 'Sure.'
    return 'Whatever.'

