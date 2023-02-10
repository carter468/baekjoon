# 다이어트
# Gold 5, 수학

G = int(input())

p = -1
for i in range(int(G**0.5),0,-1):
    if G%i==0 and i**2!=G and (a:=i+G//i)%2==0:
        print(a//2)
        p = 0
if p: 
    print(p)