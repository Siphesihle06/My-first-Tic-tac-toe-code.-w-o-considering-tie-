import random 

def GuessTheNumber():
    TargetNumber = random.randint(1,100)
    UserNumber = 0
    Guesses = 0
    print('i am thinking of a number between 1 and 100')

    while TargetNumber != UserNumber:
        UserNumber = int(input('what number am i thinking of?'))
        Guesses = Guesses+1
        if TargetNumber < UserNumber:
            print(' your guess is higher than my number')
        elif TargetNumber > UserNumber:
            print('your guess is lower than my number')
        else: 
            print('congratulations you have guessed', TargetNumber, 'in', Guesses, ' guesses')
GuessTheNumber()

