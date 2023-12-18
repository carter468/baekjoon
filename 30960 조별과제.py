# 조별 과제
# Gold 5, prefix sum, greedy

n = int(input())
arr = sorted(map(int,input().split()))

p1 = [0]
p2 = [0]
for i in range(0,n-1,2):
    p1.append(p1[-1]+arr[i+1]-arr[i])
    p2.append(p2[-1]+arr[i+2]-arr[i+1])

result = 10**9
for i in range(2,n,2):
    result = min(result,p1[i//2-1]+p2[-1]-p2[i//2]+arr[i]-arr[i-2])
print(result)