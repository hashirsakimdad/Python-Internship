# 📌 String Slicing and Simple Calculator

# Taking full name input
full_name = input("Enter your full name (First and Last): ")

# Finding space to separate first and last name
space_index = full_name.find(" ")

# Slicing first and last name
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

# Displaying sliced names
print(f"\n👤 First Name: {first_name}")
print(f"👤 Last Name: {last_name}")

# Taking two numeric inputs
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

# Performing calculations
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2 if num2 != 0 else "undefined (cannot divide by zero)"

# Displaying results with formatting
print("\n📊 Calculation Results:")
print(f"Addition: {num1} + {num2} = {add}")
print(f"Subtraction: {num1} - {num2} = {subtract}")
print(f"Multiplication: {num1} * {num2} = {multiply}")
print(f"Division: {num1} / {num2} = {divide}")
