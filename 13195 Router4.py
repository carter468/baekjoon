# Router 4
# Gold 1, constructive, ad hoc, bruteforcing

N,M,P = map(int,input().split())

for k in range(1,N+1):
    s = (N-1)//k+1
    if (N+1)*k <= M and N*s <= P: break

result = []
arr = tuple(range(N*2+1,N*2+1+k))
for i in range(N):
    result.append((i+1,arr[i//s]))
for i in range(N+1,N*2+1):
    for a in arr:
        result.append((a,i))

print(arr[-1],len(result))
for r in result: print(*r)