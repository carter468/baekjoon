# 팀원 모집
# Gold 5, bruteforcing, bitmask

n,m = map(int,input().split())
p = [list(map(int,input().split()))[1:] for _ in range(m)]

result = 11
for i in range(1,1<<m):
    solve = [0]*(n+1)
    count = bin(i).count('1')
    if count < result:
        for j in range(m):
            if i&(1<<j):
                for num in p[j]:
                    solve[num] = 1
    if sum(solve) == n: result = min(result,count)
print(result if result < 11 else -1)