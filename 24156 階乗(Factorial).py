# 階乗 (Factorial)
# Gold 5, number theory, binary search

n = int(input())

result = 0
for i in range(2,int(n**0.5)+1):
    c = 0
    while n%i == 0:
        n //= i
        c += 1
    lo,hi = 0,10**8
    while lo+1 < hi:
        mid = (lo+hi)//2
        x = 0
        j = i
        while j <= mid:
            x += mid//j
            j *= i
        if x >= c: hi = mid
        else: lo = mid
    result = max(result,hi)
print(max(result,n))