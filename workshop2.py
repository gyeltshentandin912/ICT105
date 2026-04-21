# =========================================================
# ICT105 Worksheet 2 - Sessions 3 & 4
# Author: Tony O’Shea (Tosh)
# =========================================================

print("\n================ SESSION 3 =================\n")

# =========================
# SESSION 3 - LISTS
# =========================

courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I"
]

# Original list
print("Original List:")
print(courses)

# Sorted (non-modifying)
print("\nSorted List:")
print(sorted(courses))

print("\nReverse Sorted List:")
print(sorted(courses, reverse=True))

# Reverse list
courses.reverse()
print("\nReversed List:")
print(courses)

# Sort list permanently
courses.sort()
print("\nPermanently Sorted List:")
print(courses)

# Replace a course
courses[0] = "Artificial Intelligence"
print("\nAfter Replacement:")
print(courses)

# Add new courses
courses.insert(0, "Cyber Security")
courses.insert(len(courses)//2, "Cloud Computing")
courses.append("Machine Learning")

print("\nAfter Adding Courses:")
print(courses)

# Remove 4 courses
print("\nRemoving Courses:")
removed = []
for _ in range(4):
    removed_course = courses.pop()
    removed.append(removed_course)

print("Removed Courses:", removed)
print("Remaining Courses:", courses)


# =========================
# TUPLES AND LOOPS
# =========================

print("\nTuples and Loop Section")

course_data = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I")
]

new_list = []

for course_id, course_name in course_data:
    new_list.append(course_name)

print("Extracted Course Names:")
print(new_list)


print("\n================ SESSION 4 =================\n")

# =========================
# SESSION 4 - CONDITIONALS + LOOP
# =========================

course_departments = {
    1: "Computer Science",
    2: "Mathematics",
    3: "Computer Science",
    4: "Mathematics",
    5: "Physics",
    6: "Chemistry",
    7: "Biology",
    8: "Economics",
    9: "Economics",
    10: "Psychology",
    11: "History",
    12: "English",
    13: "Philosophy",
    14: "Mathematics",
    15: "Computer Science"
}

# =========================
# SEARCH SYSTEM
# =========================

while True:
    user_input = input("\nEnter Course ID (1-15), 0 or quit: ")

    if user_input.lower() == "quit" or user_input == "0":
        print("Exiting system...")
        break

    if user_input.isdigit():
        course_id = int(user_input)

        if 1 <= course_id <= 15:
            if course_id in course_departments:
                print(f"Course ID {course_id} is in the {course_departments[course_id]} department.")
            else:
                print("Course ID not found.")
        else:
            print("Course ID is out of range (1–15), try again.")
    else:
        print(f"The value '{user_input}' has been used to exit.")
        break


# =========================
# COURSE INFORMATION SYSTEM
# =========================

print("\nCourse Information System")

course_info = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures", "Computer Science", "Programming"],
    [4, "Linear Algebra", "Mathematics", "None"]
]

user = int(input("\nEnter Course ID for details: "))

found = False

for course in course_info:
    if course[0] == user:
        print("\nCourse Details:")
        print("Course Name:", course[1])
        print("Department:", course[2])
        print("Prerequisites:", course[3])
        found = True
        break

if not found:
    print("Course ID not found.")