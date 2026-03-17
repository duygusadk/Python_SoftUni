import math

number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_attendance = 0

for i in range(number_of_students):
    attendance = int(input())
    if attendance > max_attendance:
        max_attendance = attendance

if total_lectures != 0:
    total_bonus = max_attendance / total_lectures * (5 + additional_bonus)
else:
    total_bonus = 0

print(f"Max Bonus: {math.ceil(total_bonus)}.")

print(f"The student has attended {max_attendance} lectures.")
