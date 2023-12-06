# 복면산?!
# Gold 4, bruteforcing 

import itertools

a,b,c = map(list,input().split())
i = 0
dic = {}
for x in a+b+c:
    if x not in dic:
        dic[x] = i
        i += 1

def change(x):
    temp = 0
    for a in x:
        temp = temp*10+p[dic[a]]
    return temp

if i > 10: print('NO')
else:
    for p in itertools.permutations(range(10),i):
        if change(a)+change(b) == change(c):
            print('YES')
            break
    else: print('NO')