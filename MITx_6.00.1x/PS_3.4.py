# The game
def isWordGuessed(secretWord, lettersGuessed):
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord,lettersGuessed):
    answer = []
    for char in secretWord:
        if char in lettersGuessed:
            answer.append(char)
        else:
            answer.append('_')
    return ' '.join(answer)

def getAvailableLetters(lettersGuessed):
    import string
    result = []
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            result.append(char)
    return ''.join(result)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print(f'I am thinking of a word that is {len(secretWord)} letters long.')
    print('-------------')

    guessesLeft = 8
    lettersGuessed = []
    while guessesLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print(f'You have {guessesLeft} guesses left.')
        print(f'Available letters: {getAvailableLetters(lettersGuessed)}')
        guess = str(input('Please guess a letter: '))
        guess = guess.lower()
        while len(guess) != 1 and guess not in string.ascii_lowercase:
            guess = str(input('Please guess a letter: '))
            guess = guess.lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print(f'Good guess: {getGuessedWord(secretWord,lettersGuessed)}')
            else:
                guessesLeft -=1
                print(f'Oops! That letter is not in my word: {getGuessedWord(secretWord,lettersGuessed)}')
        else:
            print(f"Oops! You've already guessed that letter: {getGuessedWord(secretWord,lettersGuessed)}")
        print('------------')
    if isWordGuessed(secretWord,lettersGuessed):
        print('Congratulations, you won!')
    else:
        print(f'Sorry, you ran out of guesses. The word was {str(secretWord)}.')

hangman('else')

