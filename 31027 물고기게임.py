# 물고기 게임
# Platinum 5, game theory, ad hoc

n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(2)]

a = sum(arr[0])
c = sum(arr[1])
b,d = 0,0
for i in range(n//2):
    b += arr[0][i]+arr[1][i]
    d += arr[0][-1-i]+arr[1][-1-i]
if n%2 == 0: d -= arr[0][n//2]+arr[1][n//2]

k = arr[0][n//2]+arr[1][n//2]
if a >= b:
    if c >= d:
        print(a,c)
    else:
        print(b+k,d)
else:
    if c >= d:
        print(b,d+k)
    else:
        print(b+k,d)