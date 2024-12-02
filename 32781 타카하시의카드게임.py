# 타카하시의 카드 게임
# Gold 3, combinatorics

MOD = 10**9+7

n = int(input())
s = input()

count = [0]*52
for c in s:
    a = ord(c)
    if a > 96:
        count[a-71] += 1
    else:
        count[a-65] += 1

result = 0
for i in range(52):
    result += pow(2,count[i],MOD)-count[i]-1
    for j in range(i+1,52):
        result = (result+count[i]*count[j])%MOD
print(result%MOD)