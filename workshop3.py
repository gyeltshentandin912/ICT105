# =========================================================
# ICT105 Worksheet 3 - Sessions 5 & 6
# Advanced Network Security
# Author: Tony O’Shea (Tosh)
# =========================================================

print("\n================ SESSION 5: DICTIONARIES ================\n")

# ---------------------------------------------------------
# 1. Student Course Enrollments
# ---------------------------------------------------------

course_enrollments = {
    "S101": ["CS101", "MA101", "PH101"],
    "S102": ["CS101", "CS102"],
    "S103": ["MA101", "EC101"],
    "S104": ["CS101", "PH101", "CH101"]
}

print("Student Course Enrollments:\n")
for student, courses in course_enrollments.items():
    print(student, "->", courses)


# ---------------------------------------------------------
# 2. Department Course Schedule
# ---------------------------------------------------------

departments = {
    "Computer Science": [("CS101", "Intro to Programming"), ("CS102", "Data Structures")],
    "Mathematics": [("MA101", "Calculus I"), ("MA102", "Linear Algebra")],
    "Physics": [("PH101", "Physics I")]
}

print("\nDepartment Course List:\n")
for dept, course_list in departments.items():
    print("\n", dept)
    for course in course_list:
        print(" ", course)


# ---------------------------------------------------------
# 3. Lecturer Assignments
# ---------------------------------------------------------

lecturer_assignments = {
    "Dr Smith": ["CS101", "CS102"],
    "Dr John": ["MA101", "MA102"],
    "Dr Sarah": ["PH101", "CH101"]
}

print("\nLecturer Assignments:\n")
for lecturer, courses in lecturer_assignments.items():
    print(lecturer, "teaches:", courses)


print("\n================ SESSION 6: USER INPUT SYSTEM ================\n")

# ---------------------------------------------------------
# 1. Course Lookup System
# ---------------------------------------------------------

courses = {
    "CS101": "Introduction to Programming",
    "CS102": "Data Structures",
    "MA101": "Calculus I",
    "PH101": "Physics I"
}

while True:
    user_input = input("\nEnter Course Code (or type quit): ")

    if user_input.lower() == "quit":
        print("Exiting Course System...")
        break

    if user_input in courses:
        print("Course Found:", courses[user_input])
    else:
        print("Course not found.")


# ---------------------------------------------------------
# 2. Student Lookup System
# ---------------------------------------------------------

students = {
    "S101": "Alice",
    "S102": "Bob",
    "S103": "Charlie",
    "S104": "David"
}

while True:
    user_input = input("\nEnter Student ID (or type quit): ")

    if user_input.lower() == "quit":
        print("System Closed.")
        break

    if user_input in students:
        print("Student Name:", students[user_input])
    else:
        print("Student not found.")