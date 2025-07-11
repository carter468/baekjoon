# 필사의 문자열
# Gold 4, greedy, bruteforcing

N = int(input())
S = input()

for i in range(25,-1,-1):
    k = chr(i+97)
    arr = []
    for j in range(N-1,-1,-1):
        if S[j] == k:
            arr.append(j)
    if not arr: continue
    for j in range(N):
        if S[j] < k:
            l = j
            break
    else: continue
    result = []
    for r in arr:
        if r > l:
            result.append(S[:l]+S[l:r+1][::-1]+S[r+1:])
    if result:
        print(sorted(result)[-1])
        break
else: print(S)