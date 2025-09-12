# Tower Defense
# Gold 1, case work, constructive

Xe,Ye = map(int,input().split())
Xh,Yh = map(int,input().split())
D = int(input())

d = abs(Xe-Xh)+abs(Ye-Yh)
if D == d:
    exit(print(0))
if D < d or (D-d)%2 == 1 or d == 1:
    exit(print('impossible'))

result = []
k = (D-d)//2-1
if Xe == Xh:
    y = (Ye+Yh)//2
    for x in range(Xe-k,Xe+k+1):
        result.append((x,y))
elif Ye == Yh:
    x = (Xe+Xh)//2
    for y in range(Ye-k,Ye+k+1):
        result.append((x,y))
elif abs(Xe-Xh) == 1:
    x1,x2 = min(Xe,Xh),max(Xe,Xh)
    y = (Ye+Yh)//2
    for x in range(x1-k,x2+k+1):
        result.append((x,y))
else:
    y1,y2 = min(Ye,Yh),max(Ye,Yh)
    x = (Xe+Xh)//2
    for y in range(y1-k,y2+k+1):
        result.append((x,y))

print(len(result))
for r in result:
    print(*r)