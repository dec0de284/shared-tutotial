print('\nHi! Welcome to my Python exercise notebook!\n')
list = ('''
\n\tPython Excercise List\n
    1. The F String\n''')

user_input = int(input(f'''Here\'s a list of my exercises. {list} 
\n Which do you want to see? '''))

def f_str():
    print('\n\tThis is the excercise for \'The F String\'\n')
    name = input('What\'s your name?\n')
    year = int(input('What\'s the year today?\n'))
    print(f'Hello {name} from the year {year}!\n')

if user_input == 1: 
    f_str()