from brain_games.games.logic import name
from random import randint

def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        def is_prime(random_number):
            for i in range(2, (random_number//2)+1):
                if random_number % i == 0:
                    return False
            return True
        if is_prime(random_number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if correct_answer == answer:
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!!".format(name))