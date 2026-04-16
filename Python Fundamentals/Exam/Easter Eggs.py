import re

text = input()

regex = r"[@,#]+([a-z]{3,})[@,#]+[^A-Za-z0-9]*\/+([0-9]+)\/+"

matches = re.findall(regex, text)

for match in matches:
    print(f"You found {match[1]} {match[0]} eggs!")
