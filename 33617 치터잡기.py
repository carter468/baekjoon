# 치터 잡기
# Platinum 4, ad hoc, constructive, implementation

N = int(input())

x,y = 1,1
result = []
if N%2 == 1:
    for i in range(N-1):
        for j in range(1,N+1):
            if x == 1:
                dx,dy = 1,-1
            else:
                dx,dy = -1,1
                j = N-j+1
            if i%2 == 0:
                dy *= -1
                j = N+1-j
            temp = []
            for k in range(1,N+1):
                if k == j:
                    y += dy
                else:
                    x += dx
                temp += [x,y]
            result.append(temp)
else:
    for i in range(N-1):
        for j in range(1,N+1):
            if x == 1:
                dx,dy = 1,-1
            else:
                dx,dy = -1,1
                j = N-j+1
            if i%2 == 0:
                dy *= -1
                j = N+1-j
            temp = []
            for k in range(1,N+1):
                if k == j:
                    y += dy
                else:
                    x += dx
                temp += [x,y]
            result.append(temp)
        y += 1
        temp = [x,y]
        dx = 1 if i%2 == 0 else -1
        for _ in range(N-1):
            x += dx
            temp += [x,y]
        result.append(temp)

print(len(result))
print(1,1)
for r in result:
    print(N,*r)