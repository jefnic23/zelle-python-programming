import math, random

def nextGuess(guess, x):
    nextguess = (guess + x/guess) / 2
    return nextguess
        
x = random.randint(1, 1000)
guess = eval(input('Guess the square root of {0}: '.format(x)))
print(math.sqrt(x) - guess)

while math.sqrt(x) - guess != 0:
    guess = nextGuess(guess, x)
    print(guess)
