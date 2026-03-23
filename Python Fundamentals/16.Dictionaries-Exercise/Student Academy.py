n = int(input())

info = {}
for i in range(n):
    student = input()
    grade = float(input())

    if student not in info.keys():
        info[student] = []

    info[student].append(grade)

for student, grade in info.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{student} -> {sum(grade) / len(grade):.2f}")

