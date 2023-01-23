# 정수 게임
# Gold 3, 비트마스킹, 포함 배제의 원리

def LCM(a,b):
    x,y = a,b
    while b!=0:
        a,b = b,a%b
    return x*y//a

N,K = map(int,input().split())
array = list(map(int,input().split()))

answer = N
for i in range(1,1<<K):
    l,count = 1,0
    for j in range(K):
        if i&(1<<j):
            count += 1
            l = LCM(l,array[j])
    answer += N//l*(-1)**(count%2)
print(answer)