# 종이 접기
# Gold 5, bruteforcing, number theory

def f(x,y):
    c = 0
    while x > y:
        x = x//2+x%2
        c += 1
    return c

W,H,A = map(int,input().split())

result = 10**9
for i in range(1,int(A**0.5)+1):
    if A%i == 0:
        j = A//i
        if i <= W and j <= H:
            result = min(result,f(W,i)+f(H,j))
        if j <= W and i <= H:
            result = min(result,f(W,j)+f(H,i))
print(result if result != 10**9 else -1)