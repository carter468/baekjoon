# 가장 긴 증가하는 팰린드롬 부분수열 
# Gold 1, 투포인터

n = int(input())
arr = tuple(map(int,input().split()))

result = 0
s = 0
while s < n:
    e = s
    if e+1 < n and arr[e+1] == arr[s]: e += 1

    l,r = s-1,e+1
    t = e-s+1

    i = arr[s]
    while l > -1 and r < n:
        if arr[l] == arr[r] and arr[l] < i:
            i = arr[l]
            l -= 1
            r += 1
            t += 2
        else:
            break

    result = max(result,t)
    s = r

print(result)