# def do_stuff(num=0):

#   try:
#     if num:
#       return int(num) + 5

#     else:
#       return 'please enter number'

#   except ValueError as err:
#     return err

from random import randint


def run_guess(guess, answer):
  if 0 < guess < 11:
    if (guess == answer):
      print('You are a genius')
      return True

  else:
    print('hey, I said 1-10')
    return False


if '__name__' == '__main__':
  #generate a number 1-10
  answer = randint(1, 10)
  #input from user?

  #check that number is a number 1-10
  while True:
    try:
      guess = int(input('guess a number 1-10: '))
      if run_guess(guess, answer):
        break
    except ValueError:
      print('please inter a number: ')
      continue

#check if the number is the right guess. Otherwise

#ask again
