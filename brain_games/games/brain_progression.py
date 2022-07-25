from brain_games.games.logic import name
from random import randint, choice


def brain_progression():
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        random_step = randint(2, 6)
        progression = list(range(0, 20, random_step))
        index = choice(progression)
        missing_item = progression[index]
        print('Question: ' + str(progression))
        answer = input('Your answer: ')
        if missing_item == int(answer):
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, missing_item))
            print("Let's try again, {}!!".format(name))
    print('Congratulations, {}!'.format(name))