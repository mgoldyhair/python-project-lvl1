#!/usr/bin/env python

import prompt
def main():
    print('Welcome to the Brain Games!')

if __name__ == '__main__':
    main()

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello,{}!'.format(name))


