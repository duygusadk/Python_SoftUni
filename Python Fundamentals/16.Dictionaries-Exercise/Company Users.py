command = input()
company = {}
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company:
        company[company_name] = []

    if employee_id not in company[company_name]:
        company[company_name].append(employee_id)

    command = input()

for key, value in company.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")
