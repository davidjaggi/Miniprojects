lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    import string
    result = []
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            result.append(char)
    return ''.join(result)


print(getAvailableLetters(lettersGuessed))
