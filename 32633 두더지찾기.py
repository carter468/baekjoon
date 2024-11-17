# 두더지 찾기
# Gold 5, number theory

def LCM(a,b):
    c = a*b
    while b:
        a,b = b,a%b
    return c//a

N,L = map(int,input().split())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))

result = 1
for i in range(N):
    if B[i] == 1:
        result = LCM(result,A[i])
        if result > L:
            print(-1)
            exit()

for i in range(N):
    if B[i] == 0:
        if result%A[i] == 0:
            result = -1
            break
print(result)