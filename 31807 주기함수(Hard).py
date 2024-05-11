# 주기 함수 (Hard)
# Platinum 4, KMP, prefix sum, math

n = int(input())
s = list(input().split())
a,b = map(int,input().split())

p = [0]*n
i = 0
for j in range(1,n):
    while i > 0 and s[i] != s[j]:
        i = p[i-1]
    if s[i] == s[j]:
        i += 1
        p[j] = i

k = n-p[-1]
arr = [0]*(k+1)
for i in range(k):
    arr[i+1] += arr[i]+int(s[i])
    
result = (b-a)//k*arr[-1]
x,y = a//k,b//k
if a < 0: a,b = a-k*x,b-k*x

c,d = a%k,b%k
if c <= d: result += arr[d]-arr[c]
else: result += arr[-1]-arr[c]+arr[d]
print(result)