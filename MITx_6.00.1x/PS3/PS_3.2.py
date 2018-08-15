# Printing out the user's guess

secretWord = 'apple'
# lettersGuessed = ['e','i','k','p','r','s']
lettersGuessed = ['a','p','p','l','e']

def getGuessedWord(secretWord,lettersGuessed):
    answer = []
    for char in secretWord:
        if char in lettersGuessed:
            answer.append(char)
        else:
            answer.append('_')
    return ' '.join(answer)

print(getGuessedWord(secretWord, lettersGuessed))