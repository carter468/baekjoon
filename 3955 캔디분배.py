# 캔디 분배
# Platinum 5, EEA

def EEA(a,b):
    if a == 0: return b,0,1
    gcd,x,y = EEA(b%a,a)
    return gcd,y-(b//a)*x,x

for _ in range(int(input())):
    K,C = map(int,input().split())
    g,x,y = EEA(K,C)

    if C == 1:
        print(K+1 if K+1 <= 10**9 else 'IMPOSSIBLE')
    elif K == 1:
        print(1)
    elif g != 1:
        print('IMPOSSIBLE')
    else:
        print(y%K)