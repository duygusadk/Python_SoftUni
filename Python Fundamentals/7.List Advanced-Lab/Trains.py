number_of_wagons = int(input())
train = []
for i in range(number_of_wagons):
    train.append(0)
command = ""
while command != "End":
    command = input()

    tokens = command.split(" ")
    if tokens[0] == "add":
        train[-1] += int(tokens[1])
    elif tokens[0] == "insert":
        train[int(tokens[1])] += int(tokens[2])

    elif tokens[0] == "leave":
        train[int(tokens[1])] -= int(tokens[2])

print(train)
