# 산타 춘배의 선물 나눠주기
# Gold 5, greedy

input()

count = [0]*4
for x in map(int,input().split()):
    count[x] += 1

result = 0
a = min(count[0],count[3])
result += a*3
count[0] -= a
count[3] -= a
b = min(count[1],count[2])
result += b*3
count[1] -= b
count[2] -= b
c = min(count[0],count[2])
result += c*2
count[0] -= c
count[2] -= c
d = min(count[1],count[3])
result += d*2
count[1] -= d
count[3] -= d
result += min(count[0],count[1])+min(count[2],count[3])
print(result)