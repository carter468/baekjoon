# Coins
# Gold 2, prefix sum

N,K = map(int,input().split())
S = input()

dic = {0:-1}
result = 0
t = 0
for i in range(N):
    if S[i] == 'R': t += K
    else: t -= 1
    if t in dic: result = max(result,i-dic[t])
    else: dic[t] = i
print(result)