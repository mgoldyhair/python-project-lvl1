from random import randint, choice

def brain_calc():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello,{}!'.format(name))
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        operations = ['*' ,'+', '-']
        operator = choice(operations)
        print('Question: ' + str(random_number1) + operator + str(random_number2))
        answer = input('Your answer: ')
        correct_answer = eval(str(random_number1) + operator + str(random_number2))
        if correct_answer == int(answer):
            print('Correct!')
            i += 1
        else:
            
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, correct_answer))
            print("Let's try again, {}!!".format(name))
    print('Congratulations, {}!'.format(name))

