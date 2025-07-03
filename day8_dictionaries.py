# Day 8 – Dictionaries Practice

# Creating a dictionary
student = {
    "name": "Hashir",
    "age": 22,
    "internship": "ProSensia Python Internship",
    "skills": ["Python", "Git", "Dictionaries"]
}

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Updating values
student["age"] = 23
student["email"] = "hashir@example.com"

# Displaying updated dictionary
print("\nUpdated Dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")
