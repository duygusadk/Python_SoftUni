import re

all_matches = []
text = input()
regex = r"\d+"
while text:
    match = re.findall(regex, text)
    if match:
        all_matches += match

    text = input()

print(" ".join(all_matches))
