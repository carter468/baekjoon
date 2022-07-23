# 부분 합

n,s = map(int,input().split())
arr = list(map(int,input().split()))

ans = 100000
start,end = 0,0   # 두 포인터
sum = arr[0]

while True:
    if sum >= s:
        ans = min(ans,end-start+1)
        sum -= arr[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        sum += arr[end]

if ans == 100000:
    print(0)
else:
    print(ans)