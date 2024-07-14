print('\n\t Hi! Welcome to my Python exercise notebook!\n')

list = ('''
\n\tPython Excercise List\n
    1. The F String\n
    2. String Index (PW recommender)\n
    3. String Methods\n
    4. String Methods Pt. 2\n''')


def f_str():
    print('\n\tThis is the excercise for \'The F String\'\n')
    name = input('What\'s your name?\n')
    year = int(input('What year were you born?\n'))
    age = 2024 - year
    print(f'Hello {name}! born in {year}. You are {age} now!\n')
    return


def indx():
    print('\n\tThis is the exercise for \'String Index\'\n')
    user_input1 = input('What\'s your username? \n')
    password = input('What\'s your password? \n')
    length = str(len(user_input1) + len(password))
    reco = ((user_input1 + length)[::-1])
    print(f'Recommended password: {reco}{length}')
    return


def strmeds():
    name = 'Aki'
    user_input1 = input(f'\n{name} is the current username. Do you want to replace it? (Y/N) \n')
    if user_input1 == 'Y' or user_input1 == 'y':
        new_name  = input('What is your name? \n')
        new_name1 = name.replace('Aki', new_name)
        print(f'\nWelcome, {new_name1}! A great adventure is just up ahead!\n')
    elif user_input1 == 'N' or user_input1 == 'n':
        print(f'\nOkay, your username remains as {name}. Best wishes on your travels!\n ')
        return


def strmeds1():
    print('\n\tCorrect the lyrics')

    lyrics = ('''
    When I was a young boy
    My father took me into the city
    To see a marching band
    He said, "Son, when you grow up
    Would you be the savior of the normies
    The uglies and the damned?" \n''')

    print(lyrics)

    wrong_lyric = str(input('What\'s the wrong word? \n'))

    if wrong_lyric in lyrics and len(wrong_lyric) >= 6:
         right_lyric = str(input('What do you want to replace it with? \n'))
         new_lyrics = lyrics.replace(wrong_lyric,right_lyric)
    else:
        print('\nThat word is not in the lyrics\n')
        return
    
    another_one = input('Is there another wrong word? (Y/N)\n')
    if another_one == 'Y' or another_one == 'y':
        wrong_lyric1 = input('What\'s the other word? \n')
        if len(wrong_lyric1) >= 6:
            right_lyric1 = input('What do you want to replace it with? \n')
            print(new_lyrics.replace(wrong_lyric1,right_lyric1))
        else:
            print('\nThat word is not in the lyrics.\n')
            return
    elif another_one == 'N' or another_one == 'n':
        print(new_lyrics)
        return


user_input = int(input(f'''Here\'s a list of my exercises. {list} 
\n Which exercise do you want to see? (Select a number) \n'''))

if user_input == 1: 
    f_str()
elif user_input == 2:
    indx()
elif user_input == 3:
    strmeds()
elif user_input == 4:
    strmeds1()
else:
    print('That is not in the list')
