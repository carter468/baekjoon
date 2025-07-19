# Divisible by 3
# Gold 1, prefix sum, math

input()
count = [[0]*3 for _ in range(3)]
result = 0
t,s = 0,0
for a in map(int,input().split()):
    count[t%3][s%3] += 1
    a %= 3
    t += a
    s += a*a
    for i in range(3):
        for j in range(3):
            if (t-i)**2%3 == (s-j)%3:
                result += count[i][j]
print(result)