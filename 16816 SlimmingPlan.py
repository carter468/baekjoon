# Slimming Plan
# Gold 5, math

a,b,c = map(int,input().split())
arr = [0]+list(map(int,input().split()))

x = b-a
for i in range(1,c+1):
    arr[i] += arr[i-1]
    if arr[i] <= x:
        print(i)
        break
else:
    if arr[-1] >= 0: print(-1)
    else:
        result = 10**10
        for i in range(1,c+1):
            result = min(result,((x-arr[i]+1)//arr[-1]+1)*c+i)
        print(result)