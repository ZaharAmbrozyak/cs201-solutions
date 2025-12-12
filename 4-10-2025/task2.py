import json

filename = 'students.json'
with open(filename, 'r') as f:
    students = json.load(f)

sorted_students = sorted(students.items(), key= lambda x: x[1], reverse=True)
grades = students.values()

max_grade = max(grades)
min_grade = min(grades)
average_grade = round(sum(grades)/len(grades), 2)

print(f"Students with the best grade, {max_grade} points")
for student, grade in students.items():
    if grade == max_grade:
        print(student)

print(f"\nStudents with the worst grade, {min_grade} points")
for student, grade in students.items():
    if grade == min_grade:
        print(student)

print(f"\nThe average grade is {average_grade}")

print("\nTop 10 students with the best grades:")
for student, grade in sorted_students[:10]:
    print(f"{student} - {grade} points")

print("\nTop 10 students with the worst grades:")
for student, grade in sorted_students[::-1][:10]:
    print(f"{student} - {grade} points")