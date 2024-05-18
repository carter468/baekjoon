# 웹 브라우저 2
# Gold 5, implementation, stack

prev = []
front = []
now = ''

n,q = map(int,input().split())
for _ in range(q):
    p = input().split()
    if p[0] == 'B':
        if prev:
            if front and front[-1][0] == now:
                front[-1][1] += 1
            else:
                front.append([now,1])
            now = prev[-1][0]
            if prev[-1][1] > 1:
                prev[-1][1] -= 1
            else:
                prev.pop()
    elif p[0] == 'F':
        if front:
            if prev and prev[-1][0] == now:
                prev[-1][1] += 1
            else:
                prev.append([now,1])
            now = front[-1][0]
            if front[-1][1] > 1:
                front[-1][1] -= 1
            else:
                front.pop()
    elif p[0] == 'A':
        if now != '':
            if prev and prev[-1][0] == now:
                prev[-1][1] += 1
            else:
                prev.append([now,1])
        now = p[1]
        front = []
    elif p[0] == 'C':
        for i in range(len(prev)):
            prev[i][1] = 1

print(now)
if prev:
    for a,b in prev[::-1]:
        for _ in range(b):
            print(a,end=' ')
    print()
else: print(-1)
if front:
    for a,b in front[::-1]:
        for _ in range(b):
            print(a,end=' ')
else:
    print(-1)