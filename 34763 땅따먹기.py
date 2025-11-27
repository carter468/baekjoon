# 땅따먹기
# Gold 4, number theory

for _ in range(int(input())):
    N,K = map(int,input().split())

    result = 'NO'
    for i in range(1,int(K**0.5)+1):
        if K%i == 0:
            if i+K//i-1 == N:
                result = 'YES'
                break
    print(result)