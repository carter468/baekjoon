# Software Licenses
# Gold 5, greedy

N = int(input())
arr = [tuple(map(float,input().split())) for _ in range(N)]

result = 0
for i in range(N):
    arr.sort(key=lambda x:x[0]*(x[1]**(i+1)-x[1]**i))
    p,r = arr.pop()
    result += p*r**i
print(f'{result+1e-9:.2f}')