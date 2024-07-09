class Colors:
    HEADER = '\033[95m'
    INFO = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Section 2: Python Introduction
# 10. Our First Python Program

print(Colors.HEADER +
      "Section 2: Python Introduction\n"
      "10. Our First Python Program" + Colors.END)

name = input("What's your name?\nName: ")  # input(), Variable

print("Hello, " + name + ".\n")  # print(), String Concatenation

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

# Section 3: Python Basics
# 21. Numbers

print(Colors.HEADER +
      "Section 3: Python Basics\n"
      "22. Math Functions" +
      Colors.END)

number = float(input("Negative Float Number: "))
print("round(): " + str(round(number)))
print("abs(): " + str(abs(number)))
