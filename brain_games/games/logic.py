import prompt


name =''
def get_name():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name
name = get_name()

