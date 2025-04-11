# 원소 합치기
# Platinum 5, greedy, bismask

def check(target):
    x = 0
    count = 0
    for a in arr:
        x |= a
        if x&target == target:
            x = 0
            count += 1
    return count >= N-K

N,K = map(int,input().split())
arr = tuple(map(int,input().split()))

answer = 0
for bit in range(30,-1,-1):
    target = answer|(1<<bit)
    if check(target): answer = target
print(answer)