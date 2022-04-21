import random

print('Welcome to guess the number!')

def guess():
  rand_num = random.randint(0,100)
  guess = 0
  while guess != rand_num:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < rand_num:
      print('Number is higher, try again')
    else: print('Number is lower, try again')
  print(f'Congrats, you guessed the correct number {rand_num}!')

play = 'y'
while play == 'y' or play == 'Y':
  play = input('Would you like to guess a number? y/n ')
  if play == 'y' or play == 'Y':
    guess()
print('Thanks for playing!')