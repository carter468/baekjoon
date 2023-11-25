# 좋은 배열 만들기
# Gold 4, case work

M = 1000001
n = int(input())
arr = sorted(map(int,input().split()))

count = [0]*M
s = 0
for a in arr:
    count[a] += 1
    s += a

result = 0

if arr[-1] == arr[-2] == arr[-3]:
    if s-arr[-1]-arr[-2] == arr[-1]*2: result = 3
elif arr[-1] == arr[-2]:
    k = s-arr[-1]*3
    if 0 < k < M: result += count[k]
    if s-arr[-1]-arr[-2] == arr[-3]*2: result += 1 
elif arr[-2] == arr[-3]:
    s -= arr[-1]
    k = s-arr[-1]
    i = 0
    while i < n-1 and arr[i]*2 <= k:
        if arr[i]*2 == k:
            c = count[arr[i]]
            result += c*(c-1)//2
            while i < n-1 and arr[i] == arr[i+1]:
                i += 1
        else:
            if 0 < k-arr[i] < M and k-arr[i] != arr[-1]:
                result += count[k-arr[i]]
        i += 1
    if s-arr[-2] == arr[-3]*2: result += 2
else:
    s -= arr[-1]
    k = s-arr[-1]
    i = 0
    while i < n-1 and arr[i]*2 <= k:
        if arr[i]*2 == k:
            c = count[arr[i]]
            result += c*(c-1)//2
            while i < n-1 and arr[i] == arr[i+1]:
                i += 1
        else:
            if 0 < k-arr[i] < M:
                result += count[k-arr[i]]
                if k-arr[i] == arr[-1]:
                    result -= 1
        i += 1
        
    s -= arr[-2]
    k = s-arr[-2]
    if 0 < k < M: result += count[k]

    if s == arr[-3]*2: result += 1

print(result)