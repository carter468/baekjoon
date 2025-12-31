# 시프트 연산
# Gold 4, constructive, greedy, bruteforcing

N = int(input())
A = input().split()

arr = [i for i in range(N) if A[i] == '1']

c1 = N-arr[0]
c2 = arr[-1]+1
if c1 < c2: result = (c1,'R'*c1)
else: result = (c2,'L'*c2)

for i in range(len(arr)-1):
    a,b = arr[i],arr[i+1]

    l = a+1
    r = N-b+l
    if l+r < result[0]:
        result = (l+r,'L'*l+'R'*r)

    r = N-b
    l = a+r+1
    if r+l < result[0]:
        result = (r+l,'R'*r+'L'*l)

print(*result,sep='\n')