# MEXchange
# Gold 1, ad hoc

N = int(input())
B = tuple(map(int,input().split()))

prev = 0
result = [0]*N
arr = set(range(1,N+1))
for i in range(N-1):
    if B[i] > i+2 or B[i] < prev:
        print('No')
        break
    prev = B[i]
    if B[i] != B[i+1]:
        result[i+1] = B[i]
        arr.remove(B[i])
else:
    if B[-1] != N+1: print('No')
    else:
        arr = sorted(arr)
        idx = 0
        for i in range(N):
            if result[i] == 0:
                result[i] = arr[idx]
                idx += 1
        print('Yes')
        print(*result)