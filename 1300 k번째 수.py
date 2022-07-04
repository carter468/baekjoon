# k번째 수

n = 3
k = 7
n = int(input())
k = int(input())

start = 1
end = k
while start<end:
    mid = (start+end)//2

    cnt = 0
    for i in range(1,n+1):
        cnt += min(mid//i,n)
    print(mid,cnt)
    input()
    if cnt < k:
        start = mid+1
    else:
        end = mid

print(start)