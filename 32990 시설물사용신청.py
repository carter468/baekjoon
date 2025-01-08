# 시설물 사용 신청
# Gold 2, greedy, constructive

N = int(input())

n = N//2
if N%2 == 0:
    count = n*n
else:
    count = n*(n+1)
print(count)

if count <= 10**6:
    for i in range(1,N):
        for j in range(1,min(i,N-i)+1):
            print((N-j)//i,end=' ')
            for k in range(j,N-i+1,i):
                print(k,k+i,end=' ')
            print()