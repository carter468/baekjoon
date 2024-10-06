# 배
# Gold 5, binary search, greedy

def check(x):
    idx = 0
    for c in crane:
        for _ in range(x):
            if idx == m: return True
            if box[idx] <= c: idx += 1
    if idx == m: return True
    return False

n = int(input())
crane = sorted(map(int,input().split()))
m = int(input())
box = sorted(map(int,input().split()))

lo,hi = 0,m
while lo+1 < hi:
    mid = (lo+hi)//2
    if check(mid): hi = mid
    else: lo = mid
print(hi if max(box) <= max(crane) else -1)
