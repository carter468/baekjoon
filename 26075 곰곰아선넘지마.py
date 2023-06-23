# 곰곰아 선 넘지마
# Gold 4, greedy

input()
S,T = input(),input()

s,t = [],[]
for i in range(len(S)):
    if S[i] == '1': s.append(i)
    if T[i] == '1': t.append(i)

c = sum([abs(s[i]-t[i]) for i in range(len(s))])
print((c//2)**2+((c+1)//2)**2)