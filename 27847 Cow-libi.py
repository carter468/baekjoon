# Cow-libi
# Gold 5, binary search

import sys,bisect
input = sys.stdin.readline

def dist(a,b,c,d):
    return (a-c)**2+(b-d)**2

g,n = map(int,input().split())
gz = sorted([tuple(map(int,input().split())) for _ in range(g)],key=lambda x:x[2])
ti = [gz[i][2] for i in range(g)]

count = 0
for _ in range(n):
    x,y,t = map(int,input().split())
    i = bisect.bisect_left(ti,t)
    if (i != 0 and dist(x,y,gz[i-1][0],gz[i-1][1]) > (gz[i-1][2]-t)**2) or (i != g and dist(x,y,gz[i][0],gz[i][1]) > (gz[i][2]-t)**2):
        count += 1
print(count)