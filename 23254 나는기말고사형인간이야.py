# 나는 기말고사형 인간이야
# Gold 5, greedy

n,m = map(int,input().split())
a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))

arr = []
for i in range(m):
    x,y = divmod(100-a[i],b[i])
    arr.append((b[i],x))
    if y: arr.append((y,1))

result = sum(a)
n *= 24
for x,y in sorted(arr)[::-1]:
    result += min(n,y)*x
    n -= y
    if n <= 0: break
print(result)
