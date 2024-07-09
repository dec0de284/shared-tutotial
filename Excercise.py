print('\nHi! Welcome to my Python excercise notebook!\n')
list = ('''
\n\tPython Excercise List\n
      1. The F String\n''')
user_input = int(input(f'Here\'s a list of my Python excercises. {list} \nWhich Python excercise do you want to see?  '))

def f_str():
    print('\n\tThis is the excercise for \'The F String\'\n')
    name = input('What\'s your name?\n')
    year = input('What\'s the year today?\n')
    print(f'Hello {name} from the year {year}!\n')

if user_input == 1: f_str()