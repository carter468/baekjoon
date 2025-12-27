# 중앙값의 함정
# Gold 5, greedy

N = int(input())
A = sorted(map(int,input().split()),reverse=True)

result = []
a = A.pop()
for _ in range((N-1)//2):
    b,c = A.pop(),A.pop()
    result.append((a,b,c))
    a = b

print(a)
for r in result: print(*r)