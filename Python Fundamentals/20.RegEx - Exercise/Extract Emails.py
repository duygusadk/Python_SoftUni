import re

text = input()
regex = r"\s(([a-z0-9]+)([\.\-\_]*)([a-z0-9]+)@([a-z0-9\-]+)(\.[a-z]+)+)\b"

matches = re.findall(regex, text)

for i in matches:
    print(i[0])
