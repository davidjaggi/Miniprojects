# Is the world guessed

secretWord = 'apple'
lettersGuessed = ['e','i','k','p','r','s']
# lettersGuessed = ['a','p','p','l','e']

def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

print(isWordGuessed(secretWord, lettersGuessed))
