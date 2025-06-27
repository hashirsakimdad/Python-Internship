# 🐍 Day 4 - Student Record System with Tuples & Sets

# -----------------------------
# Tuple: Immutable student IDs
# -----------------------------
student_ids = (101, 102, 103, 104, 105)

# Display the student IDs
print("Student IDs (Immutable):")
print(student_ids)

# -----------------------------
# Set: Unique course names
# -----------------------------
courses = {"Python", "AI", "ML"}  # Initial set of courses

print("\nInitial Course List:")
print(courses)

# -----------------------------
# Add new courses
# -----------------------------
courses.add("Data Science")  # Adding a new course
courses.add("AI")  # Duplicate won't be added

print("\nAfter Adding Courses:")
print(courses)

# -----------------------------
# Remove a course
# -----------------------------
courses.discard("ML")  # Remove an existing course

print("\nAfter Removing 'ML':")
print(courses)

# -----------------------------
# Final Summary
# -----------------------------
print("\nFinal Summary:")
print(f"Student IDs: {student_ids}")
print(f"Courses Offered: {courses}")
