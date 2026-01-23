# 주니어 개발자 동우의 직행 취업일기
# Gold 5, constructive

N = int(input())

result = [(1,2),(2,3)]
if N%2 == 0:
    result.append((2,4))
    for i in range(5,5+N//2):
        result.append((3,i))
elif N%3 == 0:
    result.append((2,4))
    result.append((2,5))
    for i in range(6,6+N//3):
        result.append((3,i))
else:
    for i in range(4,4+N):
        result.append((3,i))

print(len(result)+1)
for r in result: print(*r)