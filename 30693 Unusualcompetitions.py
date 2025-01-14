# Unusual competitions
# Gold 5, greedy

input()

result = 0
count = 0
score = 0
for c in input():
    count += 1
    if c == '(':
        score += 1
        if score == 0:
            result += count
            count = 0
    else:
        score -= 1
        if score == 0:
            count = 0
if score == 0: print(result)
else: print(-1)