
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

name = "Bhanu"
mark1 = 85
mark2 = 78
mark3 = 92

total = mark1 + mark2 + mark3
average = total / 3
grade = calculate_grade(average)

if average >= 40:
    result = "Pass"
else:
    result = "Fail"

print("----- Student Report -----")
print("Student Name:", name)
print("Marks:")
print("Subject 1:", mark1)
print("Subject 2:", mark2)
print("Subject 3:", mark3)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
print("Result:", result)
