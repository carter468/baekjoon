# List of Unique Numbers
# Gold 4, two pointer

n = int(input())
arr = tuple(map(int,input().split()))

result = 0
r = 0
count = [0]*100001
count[arr[0]] = 1
for l in range(n):
    while r < n-1 and count[arr[r+1]] == 0:
        r += 1
        count[arr[r]] = 1
    result += r-l+1
    count[arr[l]] -= 1
print(result)