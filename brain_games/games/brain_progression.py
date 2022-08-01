from brain_games.games.logic import name
from random import randint, choice


def brain_progression():
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        length = randint(5, 10)
        step = randint(2, 6)
        first_number = randint (1, 100)
        last_number = first_number + (length -1) * step
        progression = list(range(first_number, last_number, step))
        item = choice(progression)
        new_progression = str(progression).replace(str(item),'..', 1)
        print('Question: ' + str(new_progression))
        answer = input('Your answer: ')
        if item == int(answer):
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, item
            ))
            print("Let's try again, {}!!".format(name))
   