import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    num = random.randrange(10,21,2)
    return num

i = 0
while i <= 100:
    print(genEven())
    i += 1
