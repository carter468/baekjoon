# Gig Combinatorics
# Gold 5, DP

M = 10**9+7

input()
a,b,c = 0,0,0
for x in map(int,input().split()):
    if x == 1: a += 1
    elif x == 2: b = (a+b*2)%M
    else: c = (b+c)%M
print(c)