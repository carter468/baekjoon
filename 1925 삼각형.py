# 1925 삼각형
# Silver 5, 기하학

a = []
for _ in range(3):
    a.append(tuple(map(int,input().split())))

l = []
for i in range(3):
    l.append(((a[i][0]-a[i-1][0])**2+(a[i][1]-a[i-1][1])**2))
l.sort()

if (a[0][1]-a[1][1])*(a[1][0]-a[2][0])==(a[1][1]-a[2][1])*(a[0][0]-a[1][0]):
    print('X')
elif l[0]==l[1]==l[2]:
    print('JungTriangle')
elif len(set(l))==2:
    if l[2]>l[0]+l[1]:
        print('Dunkak2Triangle')
    elif l[2]==l[0]+l[1]:
        print('Jikkak2Triangle')
    else:
        print('Yeahkak2Triangle')
else:
    if l[2]>l[0]+l[1]:
        print('DunkakTriangle')
    elif l[2]==l[0]+l[1]:
        print('JikkakTriangle')
    else:
        print('YeahkakTriangle')