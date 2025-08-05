# Light Emitting Hindenburg
# Gold 4, bitmask, greedy

N,K = map(int,input().split())
arr = tuple(map(int,input().split()))

result = 0
for i in range(29,-1,-1):
    temp = []
    for a in arr:
        if a>>i&1: temp.append(a)
    if len(temp) >= K:
        result += 1<<i
        arr = temp
print(result)