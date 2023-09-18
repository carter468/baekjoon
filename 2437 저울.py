# 저울
# Gold 2, greedy

input()
result = 1
for a in sorted(map(int,input().split())):
    if a > result:
        break
    result += a
print(result)