# Know your Alines
# Gold 3, bruteforcing

import itertools

S = input()

N = len(S)
arr = []
for i in range(N-1):
    if S[i] != S[i+1]:
        arr.append(i*2+3)

c = len(arr)
result = []
for i in range(c+1):
    x = 0
    for comb in itertools.combinations(arr,i):
        y = 1
        for a in comb:
            y *= a
        x += y
    result.append(x)

i = 1 if S[-1] == 'H' else 0
while i <= c:
    result[i] *= -1
    i += 2

print(c)
print(*result)