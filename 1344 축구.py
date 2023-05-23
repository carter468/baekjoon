# 축구
# Gold 4, DP, 확률론

a = int(input())/100
b = int(input())/100
ac,bc = 1-a,1-b

dp1 = [[0]*19 for _ in range(18)]
dp1[0][1],dp1[0][0] = a,ac
dp2 = [[0]*19 for _ in range(18)]
dp2[0][1],dp2[0][0] = b,bc

for i in range(1,18):
    for j in range(19):
        dp1[i][j] += dp1[i-1][j-1]*a + dp1[i-1][j]*ac
        dp2[i][j] += dp2[i-1][j-1]*b + dp2[i-1][j]*bc

e1,e2 = 0,0
for i in (0,1,4,6,8,9,10,12,14,15,16,18):
    e1 += dp1[-1][i]
    e2 += dp2[-1][i]
print(1-e1*e2)