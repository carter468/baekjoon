# 동물원
# Gold 5, combinatorics, case work

N = int(input())
count = [0]*41
for a in map(int,input().split()):
    count[a] += 1
    
c = 0
f = True
result = 1
for i in range(41):
    c += count[i]
    if count[i] == 0:
        if c != N: result = 0
    elif count[i] == 1:
        if f: result *= 2
        f = False
    elif count[i] == 2:
        if not f: result = 0
        else: result *= 2
    else: result = 0
print(result)