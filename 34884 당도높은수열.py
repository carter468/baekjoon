# 당도 높은 수열
# Gold 4, constructive

n = 150000
result = [0]*n
result[n//2] = n
x = n-1
l,r = n//2-2,n//2+2
while l >= 0 and r < n:
    result[r] = x
    result[l] = x-1
    r += 2
    l -= 2
    x -= 2
x = 1
for i in range(n):
    if result[i] == 0:
        result[i] = x
        x += 1
print(*result)