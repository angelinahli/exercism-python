def rotate(text, key):
    return ''.join([ shift_char(char, key) for char in text])

def shift_char(char, shift):
    if char.islower():
        return chr(shift_with_base(ord(char), ord('a'), shift))
    elif char.isupper():
        return chr(shift_with_base(ord(char), ord('A'), shift))
    else:
        return char

def shift_with_base(val, base, shift):
    diff_from_base = val - base
    return ((diff_from_base + shift) % 26) + base


def another_rotate(text, key):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    end_cipher = alphabet[:key]
    start_cipher = alphabet[key:]
    cipher = start_cipher + end_cipher

    cipher_dict = dict(zip(alphabet, cipher))

    new_text = list(text)

    for i in range(len(new_text)):
        char = new_text[i]
        if char.isalpha():
            should_upper_case = char.isupper()
            new_char = cipher_dict[char.lower()]

            if should_upper_case:
                new_char = new_char.upper()

            new_text[i] = new_char

    return ''.join(new_text)