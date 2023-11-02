# 수학적인 최소 공통 조상
# Gold 5, number theory

a,b = map(int,input().split())

parent = set([a])
for i in range(2,int(a**0.5)+1):
    while a%i == 0:
        a //= i
        parent.add(a)

if b in parent:
    print(b)
    exit()

for i in range(2,int(b**0.5)+1):
    while b%i == 0:
        b //= i
        if b in parent:
            print(b)
            exit()
else:
    print(1)