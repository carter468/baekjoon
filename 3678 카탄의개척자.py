# 카탄의 개척자
# Gold 1, implementation, simulation

def check():
    s = set()
    for nx,ny in (x+1,y+1),(x,y+2),(x-1,y+1),(x-1,y-1),(x,y-2),(x+1,y-1):
        s.add(dic.get((nx,ny),-1))
        m = 99999,
        for i in range(5):
            if i not in s and count[i] < m[0]:
                m = count[i],i
    return m[1]

dic = {(0,0):0,(1,1):1}
pos = {1:(0,0),2:(1,1)}
count = [1,1,0,0,0]
x,y = 1,1
for i in range(3,10001):
    if x <= 0 and y > 0:
        if (x,y-2) in dic:
            x -= 1
            y -= 1
        else:
            y -= 2
    elif x < 0 and y <= 0:
        if (x+1,y-1) in dic:
            y -= 2
        else:
            x += 1
            y -= 1
    elif x >= 0 and y < 0:
        if (x,y+2) in dic:
            x += 1
            y += 1
        else:
            y += 2
    else:
        if (x-1,y+1) in dic:
            y += 2
        else:
            x -= 1
            y += 1

    pos[i] = (x,y)
    a = check()
    dic[(x,y)] = a
    count[a] += 1

for _ in range(int(input())):
    print(dic[pos[int(input())]]+1)