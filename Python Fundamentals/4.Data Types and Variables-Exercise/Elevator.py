total_people = int(input())
capacity = int(input())
course = 0
while total_people > 0:
    course += 1
    total_people -= capacity

print(course)