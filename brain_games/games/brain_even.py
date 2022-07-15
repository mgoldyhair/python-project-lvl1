from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello,{}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ' + str(random_number))
        answer = input('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if correct_answer == answer:
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!!".format(name))
    print('Congratulations, {}!'.format(name))
