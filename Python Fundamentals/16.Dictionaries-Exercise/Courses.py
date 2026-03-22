command = input()

register = {}
while command != "end":
    course, student_name = command.split(" : ")
    if course not in register.keys():
        register[course] = []
    register[course].append(student_name)
    command = input()

for key, value in register.items():
    print(f"{key}: {len(value)}")
    for i in value:
        print(f"-- {i}")
