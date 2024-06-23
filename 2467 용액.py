# 용액
# Gold 5, two pointer

n = int(input())
arr = tuple(map(int,input().split()))

result = [10**10]
l,r = 0,n-1
while l < r:
    a,b = arr[l],arr[r]
    if abs(a+b) < result[0]:
        result = [abs(a+b),a,b]
    
    if a+b < 0: l += 1
    elif a+b > 0: r -= 1
    else: break

print(*result[1:])