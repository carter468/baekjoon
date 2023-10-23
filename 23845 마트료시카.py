# 마트료시카
# Gold 3, greedy

input()
arr = sorted(map(int,input().split()),reverse=True)
count = [0]*(10**5+1)
for x in arr:
    count[x] += 1

result = 0
q = 0
t = 0
while arr:
    while arr and count[arr[-1]] == 0:
        arr.pop()

    if arr and q == 0:
        q = arr.pop()
        count[q] -= 1
        t = 1

    while q < len(count)-1 and count[q+1] != 0:
        q += 1
        count[q] -= 1
        t += 1

    result += q*t
    q = 0

print(result)