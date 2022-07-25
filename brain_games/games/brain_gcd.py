from brain_games.games.logic import name
from random import randint
from math import gcd 


def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        print('Question: ' + str(random_number1)+ ' ' + str(random_number2))
        answer = input('Your answer: ')
        correct_answer = gcd(random_number1, random_number2)
        if correct_answer == int(answer):
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!!".format(name))
    print('Congratulations, {}!'.format(name))


    #code