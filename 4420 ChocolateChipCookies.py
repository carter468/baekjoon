# Chocolate Chip Cookies
# Platinum 4, bruteforcing, geometry

chips = []
while True:
    try:
        chips.append(tuple(map(float,input().split())))
    except:
        break

n = len(chips)
result = 0
for i in range(n):
    x1,y1 = chips[i]
    for j in range(i+1,n):
        x2,y2 = chips[j]
        d = ((x1-x2)**2+(y1-y2)**2)**0.5
        if d > 5: continue
        mx,my = (x1+x2)/2,(y1+y2)/2
        h = (6.25-d*d/4)**0.5
        dx,dy = h*(y2-y1)/d,h*(x1-x2)/d
        for k in (1,-1):
            cx,cy = mx+dx*k,my+dy*k
            c = 0
            for x,y in chips:
                if (x-cx)**2+(y-cy)**2 <= 6.25+1e-9:
                    c += 1
            result = max(result,c)

for cx,cy in chips:
    c = 0
    for x,y in chips:
        if (x-cx)**2+(y-cy)**2 <= 6.25+1e-9:
            c += 1
    result = max(result,c)
print(result)