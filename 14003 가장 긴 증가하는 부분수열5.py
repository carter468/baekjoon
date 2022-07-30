# 가장 긴 증가하는 부분수열5

from bisect import bisect_left

n = int(input())
arr = list(map(int,input().split()))

a = []
result = []

for x in arr:
    if not a or x > a[-1]:
        a.append(x)
        result.append((len(a)-1,x))
    else:
        a[bisect_left(a,x)] = x
        result.append((bisect_left(a,x),x))

ans = []
idx = len(a) - 1
for i in range(len(result)-1,-1,-1):
    if result[i][0] == idx:
        ans.append(result[i][1])
        idx -= 1

print(len(ans))
print(*reversed(ans))