# 산책 나온 춘배
# Gold 5, case work

n,x = map(int,input().split())
arr = tuple(map(int,input().split()))

result = max(0,x-max(abs(arr[0]-arr[1]),abs(arr[-1]-arr[-2])))
for i in range(1,n-1):
    a,b,c = arr[i-1],arr[i],arr[i+1]
    if a < b < c:
        t = max(0,x-abs(a-b))
        b += t
        t += max(0,x-abs(b-c))
    elif a < b == c:
        t = max(0,x-abs(a-b))
        b += t
        t += x+abs(b-c)
    elif a < b and b > c:
        t = max(0,x-abs(b-max(a,c)))
    elif a == b < c:
        t = x+max(0,x-abs(b-c))
    elif a == b == c:
        t = x
    elif a == b > c:
        t = max(0,x-abs(b-c))
        b += t
        t += x+abs(a-b)
    elif a > b and b < c:
        t = max(0,x-abs(a-b))+max(0,x-abs(b-c))
    elif a > b == c:
        t = x+max(0,x-abs(a-b))
    elif a > b > c:
        t = max(0,x-abs(b-c))
        b += t
        t += max(0,x-abs(a-b))
    result = min(result,t)
    
print(result)