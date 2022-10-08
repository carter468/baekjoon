#1188 음식평론가

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a
        
n,m = map(int,input().split())
print(m-gcd(n,m))