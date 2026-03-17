n = int(input())
positives = []
negatives = []

for i in range(n):
    data = int(input())
    if data >= 0:
        positives.append(data)
    else:
        negatives.append(data)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
