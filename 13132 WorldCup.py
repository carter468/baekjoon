# World Cup
# Gold 4, backtracking

def betting(i,p,money):
    global result
    if i == n or money <= b:
        if money > n: result += p
        return
    betting(i+1,p*bet[i][0]/100,money*(1+m*(bet[i][1]-1)))
    betting(i+1,p*(1-bet[i][0]/100),money*(1-m))

n,m,b = map(int,input().split())
bet = [tuple(map(float,input().split())) for _ in range(n)]

m /= 100
b *= n/100
result = 0
betting(0,1,n)

print(result*100)