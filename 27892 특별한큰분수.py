# 특별한 큰 분수
# Gold 5, ad hoc

def f(x):
    return (x//2)^6 if x%2 == 0 else (x*2)^6

x,n = map(int,input().split())

s = set()
while n:
    n -= 1
    x = f(x)
    if x in s: break
    s.add(x)

if n == 0: print(x)
else:
    arr = []
    count = 0
    while x not in arr:
        count += 1
        arr.append(x)
        x = f(x)
    print(arr[n%count])