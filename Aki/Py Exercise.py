print('\n\t Hi! Welcome to my Python exercise notebook!\n')

list = ('''
\n\tPython Excercise List\n
    1. The F String\n
    2. String Index (PW recommender)\n''')

user_input = int(input(f'''Here\'s a list of my exercises. {list} 
\n Which do you want to see? '''))


def f_str():
    print('\n\tThis is the excercise for \'The F String\'\n')
    name = input('What\'s your name?\n')
    year = int(input('What\'s the year today?\n'))
    print(f'Hello {name} from the year {year}!\n')


def indx():
    print('\n\tThis is the exercise for \'String Index\'\n')
    user_input1 = input('What\'s your username? \n')
    password = input('What\'s your password? \n')
    length = str(len(user_input1) + len(password))
    reco = ((user_input1 + length)[::-1])
    print(f'Recommended password: {reco}{length}')
    
    
if user_input == 1: 
    f_str()
if user_input == 2:
    indx()