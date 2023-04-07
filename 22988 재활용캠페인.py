# 재활용 캠페인
# Gold 1, 그리디, 투포인터

n,x = map(int,input().split())
c = sorted(map(int,input().split()))

ans = 0
while n > 0 and c[n-1] == x:
    n -= 1
    ans += 1
l,r = 0,n-1
while l < r:
    if (c[l]+c[r])*2 >= x:
        ans += 1
        n -= 2
        l += 1
        r -= 1
    else:
        l += 1

print(ans + n//3)