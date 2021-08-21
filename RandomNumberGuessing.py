import random

guess = random.randint(1,9)
name = 'Harikrish'
print(name)

chances = 0 


while chances <= 5 :
    chances = chances + 1
    number = int(input('Enter your guess between 1 and 9'))
    if number == guess :
        print('Congratulations! You guessed it right!')
        break
    elif number > guess :
        print('Try again, your number was greater!')
    elif number < guess :
        print('Try again, your number was lesser!')
    if chances > 5:
        print('You lose! The number was', guess)