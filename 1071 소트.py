# 소트
# Platinum 5, greedy

input()

M = 1002
count = [0]*M
for x in map(int,input().split()):
    count[x] += 1

result = []
for i in range(M):
    if count[i]:
        if count[i+1]:
            for j in range(i+2,M):
                if count[j]:
                    result += [i]*count[i]+[j]
                    count[j] -= 1
                    break
            else:
                result += [i+1]*count[i+1]+[i]*count[i]
                count[i+1] = 0
        else:
            result += [i]*count[i]
print(*result)