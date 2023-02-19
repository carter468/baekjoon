# 나누어 질까
# Gold 1, 포함 배제의 원리, 비트마스킹

def LCM(a,b):
    c = a*b
    while b:
        a,b = b,a%b
    return c//a

N,L,R = map(int,input().split())
array = tuple(map(int,input().split()))

answer = 0
for i in range(1,1<<N):
    count = -1
    k = 1
    for j in range(N):
        if i&(1<<j):
            k = LCM(k,array[j])
            count *= -1
    answer += R//k*count - (L-1)//k*count
    
print(answer)