# 차이를 최대로 2
# Gold 2, greedy

N = int(input())
arr = sorted(map(int,input().split()))

result = 0
if N%2 == 0:
    l,r = N//2-1,N//2
    result = sum(arr[r+1:])*2+arr[r]-arr[l]-sum(arr[:l])*2
else:
    l,r = N//2-1,N//2
    result = max(result,sum(arr[r+1:])*2-arr[r]-arr[l]-sum(arr[:l])*2)
    l,r = l+1,r+1
    result = max(result,sum(arr[r+1:])*2+arr[r]+arr[l]-sum(arr[:l])*2)
print(result)