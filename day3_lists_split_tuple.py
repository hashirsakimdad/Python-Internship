# Day 3 – Working with Lists, Split/Join, and Tuples

# 1. Take sentence input from the user
sentence = input("Enter a sentence: ")

# 2. Split the sentence into a list of words
words_list = sentence.split()

# 3. Print the list of words
print("\nList of words:")
print(words_list)

# 4. Join the list back into a sentence using ' - ' as a separator
joined_sentence = ' - '.join(words_list)
print("\nJoined sentence with '-' separator:")
print(joined_sentence)

# 5. Store first and last name in a tuple
name_tuple = ("Hashir", "Sakimdad")

# 6. Print each part using indexing
print("\nFirst and Last Name from tuple:")
print(f"First Name: {name_tuple[0]}")
print(f"Last Name: {name_tuple[1]}")
