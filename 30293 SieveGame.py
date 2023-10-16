# Seive Game
# Gold 5, greedy, number theory

n = int(input())
arr = tuple(map(int,input().split()))

count = 0
result = [0]*n
for i in range(1,n+1):
    if arr[i-1] != result[i-1]:
        k = arr[i-1]-result[i-1]
        count += abs(k)
        for j in range(i+i,n+1,i):
            result[j-1] += k
print(count)