# Printer's Head
# Gold 5, greedy

n = int(input())
arr = [0]*(n+1)
for i,a in enumerate(map(int,input().split())):
    arr[a] = i

result = 1
i = 1
while i < n-1:
    if (arr[i]-arr[i+1])*(arr[i+1]-arr[i+2]) < 0:
        result += 1
        i += 1
    i += 1
print(result)