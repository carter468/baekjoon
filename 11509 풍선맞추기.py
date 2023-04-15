# 풍선 맞추기
# Gold 5, 그리디

input()
a = [0]*1000001
c = 0
for h in map(int,input().split()):
    if a[h]:
        a[h] -= 1
        a[h-1] += 1
    else:
        c += 1
        a[h-1] += 1

print(c)