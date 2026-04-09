# Student Grade Calculator Project

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

name = input("Enter student name: ")

mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3
grade = calculate_grade(average)

print("\n----- Student Report -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
