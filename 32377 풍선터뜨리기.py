# 풍선 터뜨리기
# Gold 3, binary search

def check(t):
    return t//x + t//y + t//z >= N

N,x,y,z = map(int,input().split())

lo,hi = 0,10**18
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid

a = lo//x+lo//y+lo//z
p = 'C'
if hi%x == 0:
    a += 1
    if a == N: p = 'A'
if hi%y == 0:
    a += 1
    if a == N: p = 'B'
print(p,'win')