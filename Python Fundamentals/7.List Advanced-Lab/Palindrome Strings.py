strings = input().split(" ")
searched_palindrome = input()

palindromes = [word for word in strings if "".join(reversed(word)) == word]

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")
