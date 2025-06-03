# SKK 문자열
# Gold 2, prefix sum

S = input()

N = len(S)
arr = [0]*N
for i in range(N):
    arr[i] += arr[i-1]
    if S[i] == 'S': arr[i] += 2
    elif S[i] == 'K': arr[i] -= 1

idx = {0:-1}
for i in range(N):
    if arr[i] not in idx:
        idx[arr[i]] = i

result = -1
p = -1
for i in range(N):
    j = idx[arr[i]]
    if j < p: result = max(result,i-j)
    if S[i] in 'SK': p = i
print(result)