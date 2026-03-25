text = input()
final_text = ""

for i in text:
    if not final_text or i != final_text[-1]:
        final_text += i

print(final_text)
