# Day 7 – ProSensia Python Internship
# Topic: Loops, enumerate(), and sort()

# 1️ Using a while loop to get valid input
print("Welcome! Let's collect 3 fruits you like.")

fruits = []
count = 0

while count < 3:
    fruit = input(f"Enter fruit #{count + 1}: ").strip()
    if fruit:
        fruits.append(fruit)
        count += 1
    else:
        print("⚠️ Please enter a valid fruit name.")

# 2️ Using enumerate() to display indexed fruit list
print("\n Your Fruits (with index):")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 3️ Sorting the fruit list alphabetically
fruits.sort()
print("\n Sorted Fruit List:")
for fruit in fruits:
    print(f" {fruit}")

# 4️ Nested loop: Displaying multiplication table for 2 and 3
print("\n Multiplication Table (2x1 to 3x3):")
for i in range(2, 4):  # 2 and 3
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("---")

# 5️ Summary
print("\n Task Completed! You used while loops, for loops, nested loops, enumerate(), and sort().")
