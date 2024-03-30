# 나는 정말 휘파람을 못 불어
# Gold 4, combinatorics, prefix sum

MOD = 10**9+7

n = int(input())
s = input()

w,e,h = [0]*n,[0]*n,[]
for i in range(n):
    w[i],e[i] = w[i-1],e[i-1]
    if s[i] == 'W': w[i] += 1
    elif s[i] == 'E': e[i] += 1
    elif s[i] == 'H': h.append(i)

result = 0
for i in h:
    a = w[i]
    b = e[-1]-e[i]
    result = (result+a*((1<<b)-1-b))%MOD
print(result)