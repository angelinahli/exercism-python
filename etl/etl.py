def transform(legacyDct):
    """legacyDct contains numbers as keys and letter lists as values"""
    newDct = {}
    for score in legacyDct:
        for letter in legacyDct[score]:
            newDct[letter.lower()] = score
    return newDct
