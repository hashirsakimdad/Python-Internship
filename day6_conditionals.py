# Day 6 – Conditional Logic Practice (Pro Version)

def classify_user(name: str, age: int):
    if age < 0 or age > 130:
        return f" {name}, please enter a valid age."
    
    if age < 13:
        category = "a Child "
    elif age < 20:
        category = "a Teenager "
    elif age < 60:
        category = "an Adult "
    else:
        category = "a Senior Citizen "

    return f"Hello {name.title()}! You are classified as {category}"

# Taking user input
try:
    name_input = input("Enter your name: ").strip()
    age_input = int(input("Enter your age: "))

    result = classify_user(name_input, age_input)
    print("\n" + result)

except ValueError:
    print("\n Invalid input. Age must be a number.")
