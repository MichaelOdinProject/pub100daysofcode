# convert scores to grades
# output new dict called student_grades
# This should have student names: grades

# Criteria:
# (Scores : Grade)
# 91 - 100: Outstanding
# 81-90: Exceeds Expectation
# 71-80: Accpetable
# =<70: Fail

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Hagrid": 103,
    "Snape": -2
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 91 and score <= 100:
        student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score >= 71 and score <= 80:
        student_grades[student] = "Acceptable"
    elif score <= 70 and score >= 0:
        student_grades[student] = "Fail"

print(student_grades)

# cleaner print
print("Student------Grades")
for student in student_grades:
    print(f"{student}: {student_grades[student]}")
