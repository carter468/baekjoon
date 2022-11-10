# 원상 복구 (small)

def reverse_suffle():
    temp = [0]*n
    for i in range(n):
        temp[d[i]-1] = s[i]
    s[:] = temp[:]

n,k = map(int,input().split())
s = list(map(int,input().split()))
d = list(map(int,input().split()))
for _ in range(k):
    reverse_suffle()
print(*s)