n = int(input())
word = input()
sentences = []
for i in range(n):
    string = input()
    sentences.append(string)
print(sentences)
for j in range(len(sentences) - 1, -1, -1):
    if word not in sentences[j]:
        sentences.remove(sentences[j])
print(sentences)
