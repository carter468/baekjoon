# 하이터치☆메모리
# Gold 4, prefix sum, ad hoc

from collections import defaultdict

A,B = input(),input()

count = defaultdict(int)
m,c = 0,0
for b in B:
    if b == '(': c += 1
    else: c -= 1
    if c <= m: count[c] += 1
    m = min(m,c)

result = 0
c = 0
for a in A:
    if a == '(': c += 1
    else: c -= 1
    if c < 0: break
    result += count[-c]
print(result)