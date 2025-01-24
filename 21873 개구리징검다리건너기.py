# 개구리 징검다리 건너기
# Gold 1, ad hoc, constructive

N = int(input())

result = []

# PHASE 1
for i in range(1,N+1):
    k = i%2
    for j in range(1,i+1):
        result.append((2-k,j))

# PHASE 2
t = N%2
arr = [0,0]
arr[1-t] = 1
while arr[0] <= N or arr[1] <= N:
    for i in range(max(1,arr[t]),N+1):
        result.append((1+t,i))
    arr[t] += 2
    t = 1-t

print(len(result))
for r in result:
    print(*r)