# Field Reduction (Silver)
# Gold 3, bruteforcing

import sys,itertools
input = sys.stdin.readline
INF = sys.maxsize

p = [tuple(map(int,input().split())) for _ in range(int(input()))]

arr = set()
for f in (lambda x:x[0]),(lambda x:x[1]):
    p.sort(key=f)
    for i in range(3):
        arr.add(p[i])
        arr.add(p[-1-i])

result = INF
for c in itertools.combinations(arr,3):
    mx,my,Mx,My = INF,INF,0,0
    for x,y in p:
        if (x,y) not in c:
            mx,my,Mx,My = min(mx,x),min(my,y),max(Mx,x),max(My,y)
    result = min(result,(Mx-mx)*(My-my))
print(result)