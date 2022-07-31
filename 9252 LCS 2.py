# LCS 2

s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)

lcs = [['']*(l2+1) for _ in range(l1+1)]

for i in range(l1):
    for j in range(l2):
        if s1[i] == s2[j]:
            lcs[i+1][j+1] = lcs[i][j] + s1[i]
        else:
            if len(lcs[i][j+1]) >= len(lcs[i+1][j]):
                lcs[i+1][j+1] = lcs[i][j+1]
            else:
                lcs[i+1][j+1] = lcs[i+1][j]

print(len(lcs[-1][-1]))
print(lcs[-1][-1])
