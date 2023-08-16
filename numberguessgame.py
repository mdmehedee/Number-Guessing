
from random import randint

#generate a number 1-10
answer: int = randint(1,10)
#input from user?

#check that number is a number 1-10
while True:
    try:
        guess = int(input('guess a number 1-10: '))
        if (0<guess<11):
            if (guess == answer):
                print('You are a genius')
                break

        else:
            print('hey, I said 1-10')

    except ValueError:
        print('please inter a number: ')
        continue

#check if the number is the right guess. Otherwise

#ask again

