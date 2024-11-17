# gcd와 최단 경로
# Gold 4, ad hoc

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

k,n = map(int,input().split())

count = 0
for i in range(1,n+1):
    if i != k and gcd(k,i) <= 2: count += 1
print(count)