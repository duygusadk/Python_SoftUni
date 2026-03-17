string_version = input().split(".")
version = []
for i in string_version:
    version.append(int(i))

version[2] += 1
if version[2] == 10:
    version[2] = 0
    version[1] += 1
    if version[1] == 10:
        version[1] = 0
        version[0] += 1

string_version.clear()
for i in version:
    string_version.append(str(i))
print(".".join(string_version))
