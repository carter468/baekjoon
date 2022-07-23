# 두 수의 합

n = int(input())    # 수의 개수
arr = list(map(int,input().split()))    # 수열
x = int(input())    # a[i]+a[j] = x

arr.sort()
start,end = 0,n-1   # 투 포인터
cnt = 0             # 카운팅

while start<end:
    if arr[start] + arr[end] == x:
        cnt += 1
        start += 1
        end -= 1
    elif arr[start] + arr[end] > x:
        end -= 1
    else:
        start += 1

print(cnt)