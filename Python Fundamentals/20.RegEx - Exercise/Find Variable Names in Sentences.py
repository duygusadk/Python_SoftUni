import re

text = input()
regex = r"\b_([A-Za-z0-9]+)\b"

matches = re.findall(regex, text)

print(f",".join(matches))
