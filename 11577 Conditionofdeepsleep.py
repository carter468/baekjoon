# Condition of deep sleep
# Gold 3, greedy, prefix sum

N,K = map(int,input().split())
S = tuple(map(int,input().split()))

count = 0
arr = [0]*(N+1)
for i in range(N-K+1):
    arr[i] += arr[i-1]
    if (S[i]+arr[i])%2 == 1:
        count += 1
        arr[i] += 1
        arr[i+K] -= 1
for i in range(N-K+1,N):
    arr[i] += arr[i-1]
    if (S[i]+arr[i])%2 == 1:
        print('Insomnia')
        break
else: print(count)