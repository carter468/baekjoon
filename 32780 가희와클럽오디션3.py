# 가희와 클럽 오디션 3
# Gold 4, combinatorics

MOD = 10**9+7

def nCr(n,r):
    x = 1
    for i in range(r):
        x *= (n-i)
        x //= i+1
    return x

lv = int(input())

if lv < 6:
    print(4**lv)
else:
    result = 0
    for i in range(7):
        result += pow(8,lv-i,MOD)*(8**i)*nCr(lv,i)%MOD
    print(result%MOD)