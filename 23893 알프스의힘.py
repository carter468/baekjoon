# 알프스의 힘
# Platinum 3, number theory

N,P,K = map(int,input().split())
A = tuple(map(int,input().split()))

count = dict()
for a in A:
    b = (a**3-a*K)%P
    count[b] = count.get(b,0)+1

result = 0
for c in count.values():
    result += c*(c-1)//2
print(result)