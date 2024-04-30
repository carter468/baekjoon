# 물병
# Gold 5, greedy

n,k = map(int,input().split())

for i in range(k):
    a = 1
    while a < n:
        a *= 2
    if i != k-1:
        n -= a//2
print(a-n)