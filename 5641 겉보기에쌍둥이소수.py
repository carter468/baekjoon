# 겉보기에 쌍둥이 소수
# Gold 4, number theory

M = 8000
seive = [True]*M
for i in range(2,int(M**0.5)+1):
    if seive[i]:
        for j in range(i*i,M,i):
            seive[j] = False

x = 1
for i in range(2,M):
    if seive[i]:
        x *= i
x = str(x)

while True:
    n,t = map(int,input().split())
    if n == 0: break
    print(x+'0'*(n-3425)+'8009')