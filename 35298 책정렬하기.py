# 책 정렬하기
# Platinum 5, constructive, implementation

N = int(input())
A = list(map(int,input().split()))

result = []
for i in range(N,1,-1):
    for j in range(N):
        if A[j] == N:
            break
    if (N-j)%2 == 1:
        c = (N-j)//2
        result.extend([N-1]*c)
        B = A[j+1:]+A[:j+1]
    else:
        if i == 2: exit(print('NO'))
        if N%2 == 0:
            if j == 0:
                result.append(N-1)
                A = A[-2:]+A[:-2]
                j = 2
            result.append(j)
            c = N//2-1
            result.extend([N-1]*c)
            A = A[j-1:j+1]+A[:j-1]+A[j+1:]
            B = A[2:]+A[:2]
        else:
            result.append(j+1)
            c = N//2
            A = A[j:j+2]+A[:j]+A[j+2:]
            B = []
            result.extend([N-1]*c)
            B = A[1:]+A[:1]
    N -= 1
    A = B[:-1]

print('YES')
print(len(result))
print(*result)