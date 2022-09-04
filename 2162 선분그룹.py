#선분그룹 pypy3

import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    return x1*y2 + x2*y3 + x3*y1 - (x2*y1 + x3*y2 + x1*y3)

def check(i,j):     # 만나는지 체크
    x1,y1,x2,y2 = lines[i][0],lines[i][1],lines[i][2],lines[i][3]
    x3,y3,x4,y4 = lines[j][0],lines[j][1],lines[j][2],lines[j][3]
    abc = ccw(x1,y1,x2,y2,x3,y3)
    abd = ccw(x1,y1,x2,y2,x4,y4)
    cda = ccw(x3,y3,x4,y4,x1,y1)
    cdb = ccw(x3,y3,x4,y4,x2,y2)
    mx1, my1, mx2, my2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
    mx3, my3, mx4, my4 = min(x3, x4), min(y3, y4), max(x3, x4), max(y3, y4)
    ans = False
    if abc*abd == 0 and cda*cdb == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            ans = True
    elif abc*abd <= 0 and cda*cdb <= 0:
        ans = True
    return ans

def find(x):    # root를 찾는다
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x,y): # 두 집합을 합친다
    x = find(x)
    y = find(y)
    root[x] = y
    cnt[y] += cnt[x]

n = int(input())
lines = []
root = [i for i in range(n+1)]      # root 저장용
cnt = [1]*(n+1)                     # 같은 그룹의 선분 개수
for i in range(1,n+1):
    lines.append(list(map(int,input().split())))
    for j in range(1,i):
        if find(i) != find(j):      # 같은 그룹에 있지 않다면
            if check(i-1,j-1):      # 같은 그룹인지 확인후 맞으면
                union(i,j)          # 합친다
    
ans = 0
for i in range(1,n+1):  # root의 수(group의 수) 세기
    if root[i] == i:
        ans += 1

print(ans)
print(max(cnt))