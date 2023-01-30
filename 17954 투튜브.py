# 투튜브
# Gold 2, 구성적, 그리디 알고리즘

N = int(input())

tube = *tuple(range(2*N-3,N-2,-1)),2*N-2,2*N-1,*tuple(range(N-2,0,-1)),2*N
t,result = 0,0
left_size = (2*N)*(2*N+1)//2

for size in tube:
    result += (left_size:=left_size-size)*(t:=t+1)
if N==1:
    result = 2

print(result)
if N>1:
    print(*tube[:N])
print(*tube[N:])