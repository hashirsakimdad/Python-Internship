# Day 9 – File & Exception Handling

try:
    # Writing to a file
    with open("notes.txt", "w") as file:
        file.write("Today I learned about file handling and exception handling!")

    # Reading from the file
    with open("notes.txt", "r") as file:
        content = file.read()
        print("File Content:", content)

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You don't have permission to access the file.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
