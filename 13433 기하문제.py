# 기하 문제
# Gold 1, bruteforcing, geometry

import itertools

input()
m = 1<<34
for p in itertools.permutations(map(int,input().split())):
    c = []
    for a in p:
        x = 0
        for px,py in c:
            x = max(x,px+(4*a*py)**0.5)
        c.append((x,a))
    m = min(m,c[-1][0]-c[0][0])
print(m)