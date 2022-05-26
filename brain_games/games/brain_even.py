import prompt
from random import randint

def welcome():
    print('Welcome to the Brain Games!')

name = ''
def get_users_name():
    name = prompt.string('May I have your name? ')

users_name = get_users_name()

def greetings():
    print('Hello,{}!'.format(users_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

def brain_even():
    i = 0
    while i <= 3:
        random_number = randint(1, 100)
        correct_answer = ''
        if random_number % 2 == 0:
            correct_answer = 'yes' 
        else:
            correct_answer = 'no'
        print('Question: ' + str(random_number))
        answer = input()
        print('Your answer: answer')
        if correct_answer == answer:
            print('Correct!')
        i = i + 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!!".format(users_name))
        i = i 
    print('Congratulations, {}!'.format(users_name))
    