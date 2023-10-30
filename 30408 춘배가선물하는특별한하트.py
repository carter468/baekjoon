# 춘배가 선물하는 특별한 하트
# Gold 5, math

n,m = map(int,input().split())

if n == m: print('YES')
else:
    l,r = m,m
    while r < n:
        l = l*2-1
        r = r*2+1
        if l <= n <= r:
            print('YES')
            break
    else:
        print('NO')