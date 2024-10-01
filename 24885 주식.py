# 주식
# Gold 4, greedy, implementation

n,m,k = map(int,input().split())
arr = tuple(map(int,input().split()))

result,p,c = 0,0,0
for i in range(n-2):
    m += c*arr[i]
    result = max(result,m) 
    m -= p
    c,p = 0,0
    if arr[i] > arr[i+1] or m*(k+1) < arr[i]: continue 
    p = m*k 
    m += p
    c,m = divmod(m,arr[i])

m += c*arr[-2]
result = max(result,m)
m -= p
if m*(k+1) < arr[-2]:
    print(result)
else:
    a = m*(k+1)
    c,a = divmod(a,arr[-2])
    a += c*arr[-1]
    print(max(result,a))
