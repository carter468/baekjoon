# 고냥이
# Gold 4, two_pointer

from collections import defaultdict

n = int(input())
s = input()

count = defaultdict(int)
l,r = 0,0
count[s[l]] = 1
c = 1
result = 1

while r < len(s):
    if c <= n:
        result = max(result,r-l+1)
        r += 1
        if r < len(s):
            count[s[r]] += 1
            if count[s[r]] == 1: c += 1
    else:
        count[s[l]] -= 1
        if count[s[l]] == 0: c -= 1
        l += 1

print(result)