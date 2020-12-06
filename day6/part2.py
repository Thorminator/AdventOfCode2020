with open("input.txt") as f:
    groups = f.read().split("\n\n")

res = 0
for group in groups:
    answers = group.split("\n")
    res += sum(1 for letter in answers[0] if all(letter in answer for answer in answers))
print(res)
