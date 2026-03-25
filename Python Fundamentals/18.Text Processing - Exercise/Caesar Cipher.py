text = input()
encrypted_text=""
for ch in text:
    encrypted_version = chr(ord(ch) + 3)
    encrypted_text+=encrypted_version

print(encrypted_text)
