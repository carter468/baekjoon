# 토너먼트 만들기
# Gold 4, greedy

n = int(input())
arr = list(map(int,input().split()))

result = 0
for i in range(n,1,-1):
    idx = arr.index(i)
    if idx == 0:
        result += arr[idx]-arr[idx+1]
    elif idx == len(arr)-1:
        result += arr[idx]-arr[idx-1]
    else:
        result += min(arr[idx]-arr[idx-1],arr[idx]-arr[idx+1])
    arr.remove(i)
print(result)