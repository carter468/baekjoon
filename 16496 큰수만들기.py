# 큰 수 만들기
# Platinum 5, greedy

input()
arr = []
for a in input().split():
    b = a
    while len(b) < 10:
        b += a
    arr.append((int(b[:10]),int(a)))
result = ''
for b,a in sorted(arr)[::-1]:
    result += str(a)
print(int(result))