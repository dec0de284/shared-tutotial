# Section 2: Python Introduction
# 10. Our First Python Program

print("\n"
      "Section 2: Python Introduction\n"
      "10. Our First Python Program\n")

name = input("What's your name?\nName: ")  # input(), Variable

print("Hello, " + name + ".")  # print(), String Concatenation

# Section 3: Python Basics
# 21. Numbers

print("\n"
      "Section 3: Python Basics\n"
      "21. Numbers\n"
      "\n")

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
      "Type: " + str(type(value)))
