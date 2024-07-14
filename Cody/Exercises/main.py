from datetime import datetime


# region Console Colors
class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# endregion

# region Section 2, #10
# Section 2: Python Introduction
# 10. Our First Python Program

print(Colors.HEADER +
      "Section 2: Python Introduction\n"
      "10. Our First Python Program" + Colors.END)

name = input("What's your name?\nName: ")  # input(), Variable

print("Hello, " + name + ".\n")  # print(), String Concatenation

# endregion

# region Section 3, #21
# Section 3: Python Basics
# 21. Numbers

print(Colors.HEADER +
      "Section 3: Python Basics\n"
      "21. Numbers" +
      Colors.END)

first_number = input("First Number: ")
second_number = input("Second Number: ")

# Addition, type()
value = int(first_number) + int(second_number)
print("\n"
      "Addition: " + first_number + " + " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Subtraction, type()
value = int(first_number) - int(second_number)
print("\n"
      "Subtraction: " + first_number + " - " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Multiplication, type()
value = int(first_number) * int(second_number)
print("\n"
      "Subtraction: " + first_number + " * " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Division, type()
value = int(first_number) / int(second_number)
print("\n"
      "Subtraction: " + first_number + " / " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Exponential, type()
value = int(first_number) ** int(second_number)
print("\n"
      "Subtraction: " + first_number + " ** " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Floor Division, type()
value = int(first_number) // int(second_number)
print("\n"
      "Subtraction: " + first_number + " // " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)))

# Modulo, type()
value = int(first_number) % int(second_number)
print("\n"
      "Subtraction: " + first_number + " % " + second_number + " = " + str(value) + "\n" +
      "Type: " + str(type(value)) + "\n")

# endregion

# region Section 3, #22
# Section 3: Python Basics
# 22. Math Functions

print(Colors.HEADER +
      "Section 3: Python Basics\n"
      "22. Math Functions" +
      Colors.END)

number = float(input("Negative Float Number: "))
print("round(): " + str(round(number)))
print("abs(): " + str(abs(number)) + '\n')

# endregion

# region Section 3, #28
# Section 3: Python Basics
# 28. Variables

print(Colors.HEADER +
      "Section 3: Python Basics\n"
      "28. Variables" +
      Colors.END)

string1, string2, string3 = "This", "is sample of", "Tuple Unpacking"
print(string1)
print(string2)
print(string3)
input(Colors.WARNING + "Press ENTER to continue..." + Colors.END + '\n')

# endregion

# region Section 3, #30
# Section 3: Python Basics
# 30. Augmented Assignment Operator

print(Colors.HEADER +
      "Section 3: Python Basics\n"
      "30. Augmented Assignment Operator" +
      Colors.END)

first_number = input("First Number: ")
second_number = input("Second Number: ")

# Addition
value = int(first_number)
value += int(second_number)
print("\n"
      "Addition: " + first_number + " += " + second_number + " = " + str(value) + "\n")

# Subtraction
value = int(first_number)
value -= int(second_number)
print("\n"
      "Subtraction: " + first_number + " -= " + second_number + " = " + str(value) + "\n")

# Multiplication
value = int(first_number)
value *= int(second_number)
print("\n"
      "Multiplication: " + first_number + " *= " + second_number + " = " + str(value) + "\n")

# Division
value = int(first_number)
value /= int(second_number)
print("\n"
      "Division: " + first_number + " /= " + second_number + " = " + str(value) + "\n")

# Exponential
value = int(first_number)
value **= int(second_number)
print("\n"
      "Exponential: " + first_number + " **= " + second_number + " = " + str(value) + "\n")

# Floor Division, type()
value = int(first_number)
value //= int(second_number)
print("\n"
      "Floor Division: " + first_number + " //= " + second_number + " = " + str(value) + "\n")

# Modulo, type()
value = int(first_number)
value %= int(second_number)
print("\n"
      "Modulo: " + first_number + " %= " + second_number + " = " + str(value))

# endregion

# region Section 3, #31
# Section 3: Python Basics
# 31. Strings

header_string = '''
{color_header}Section 3: Python Basics
31. Strings{color_end}
'''
print(header_string.format(color_header=Colors.HEADER, color_end=Colors.END))

string_content = '''Welcome, {user}.
This is a sample long string.'''
print(string_content.format(user=name))

press_enter_notice = '''{color_header}Press ENTER to continue...{color_end}'''
input(press_enter_notice.format(color_header=Colors.WARNING, color_end=Colors.END))

# endregion

# region Section 3, #35
# Section 3: Python Basics
# 35. Formatted Strings

print(f'''
{Colors.HEADER}Section 3: Python Basics
35. Formatted Strings{Colors.END}''')

print(f'''Hi {name}, this is a sample long string with String Interpolation.''')

input(f'''{Colors.WARNING}Press ENTER to continue...{Colors.END}''')

# endregion

# region Section 3, #36
# Section 3: Python Basics
# 36. String Indexes

print(f'''
{Colors.HEADER}Section 3: Python Basics
36. String Indexes{Colors.END}''')

string = "cQjQNKtAC9jA6aWhXBNkaD7K"

print(f'''Original String: {string}
Limit to 12 characters: {string[:12]} - Length: {len(string[:12])}
Reverse string: {string[::-1]}''')

input(f'''{Colors.WARNING}Press ENTER to continue...{Colors.END}''')

# endregion

# region Section 3, #40
# Section 3: Python Basics
# 40. Exercise: Type Conversion

print(f'''
{Colors.HEADER}Section 3: Python Basics
40. Exercise: Type Conversion{Colors.END}''')

# https://docs.python.org/3/library/datetime.html
input_birth_year = datetime.strptime(input("What's your year of birth>\nYear: "), "%Y")
age = int((datetime.now() - input_birth_year).total_seconds() // 31_556_952)
print(f'''You're now {age} years old.''')
input(f'''{Colors.WARNING}Press ENTER to continue...{Colors.END}''')

# endregion

# region Section 3, #42
# Section 3: Python Basics
# 42. Exercise: Password Checker

print(f'''
{Colors.HEADER}Section 3: Python Basics
42. Exercise: Password Checker{Colors.END}''')

username = "Cody"
password = "123"
input_username = input("What's your username?\nUsername: ")
if input_username == username:
    print(f"Welcome, {username}. Your password is {'*' * len(password)} and {len(password)} characters long.")
    input_password = input("What's your password?\nPassword: ")
    if input_password == password:
        print(f'{Colors.GREEN}Success login!{Colors.END}')
    else:
        print(f'{Colors.RED}Wrong password!{Colors.END}')
else:
    print(f"{Colors.RED}No existing user!{Colors.END}")

# endregion

# region Section 3, #45
# Section 3: Python Basics
# 45. Matrix

print(f'''
{Colors.HEADER}Section 3: Python Basics
45. Matrix{Colors.END}''')

numbers = [[2, 8, 4], [1, 7, 5]]
even_numbers = numbers[0]
odd_numbers = numbers[1]
print(f"Even Numbers: {even_numbers}")
print(f"Odd Nubmers: {odd_numbers}")

# endregion

# region Section 3, #46
# Section 3: Python Basics
# 46. List Methods

print(f'''
{Colors.HEADER}Section 3: Python Basics
46. List Methods{Colors.END}''')

my_list = []

my_list.append('meow')  # ['meow']
print(my_list)
my_list.insert(0, 'first')  # ['first','meow']
print(my_list)
my_list.extend(['count', 1])  # ['first','meow','count',1]
print(my_list)
my_list.pop()  # ['first','meow','count']
print(my_list)
my_list.pop(0)  # ['meow','count']
print(my_list)
my_list.remove('count')  # ['meow']
print(my_list)
my_list.clear()  # []
print(my_list)

# endregion

# region Section 3, #47
# Section 3: Python Basics
# 47. List Methods 2
print(f'''
{Colors.HEADER}Section 3: Python Basics
47. List Methods 2{Colors.END}''')

my_list = ['first', 'meow', 'count', 1]

print(my_list.index('meow'))
if 'count' in my_list:
    print('meow count: ' + str(my_list[3]))

print(str(my_list).count('o'))  # counted how many letter 'o' in my_list

# endregion

# region Section 3, #48
# Section 3: Python Basics
# 48. List Methods 3
print(f'''
{Colors.HEADER}Section 3: Python Basics
48. List Methods 3{Colors.END}''')

my_list = ['first', 'meow', 'count']

my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
# endregion
