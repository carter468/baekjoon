# 팀 배정
# Gold 3, greedy

for _ in range(int(input())):
    N,K = map(int,input().split())
    A = tuple(map(int,input().split()))
    B = tuple(map(int,input().split()))

    x = sum(A)
    result = 0
    for i,d in enumerate(sorted([a-b for a,b in zip(A,B)]),1):
        x -= d
        if abs(N-i*2) <= K:
            result = max(result,x)

    print(result)