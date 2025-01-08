# 트리를 안 쓰는 트리 문제
# Gold 2, greedy, constructive

N = int(input())

print(N*2-1)
print(1,N,1,1)
for i in range(1,N):
    print(N*i+1,N*i+i,i+1,N-i+1)
    print(N*i+i+1,N*(i+1),i+1,1)