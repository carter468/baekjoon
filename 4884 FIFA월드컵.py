# FIFA 월드컵

while True:
    g,t,a,d = map(int,input().split())
    if [g,t,a,d] == [-1,-1,-1,-1]:
        break
    w = g*a+d
    z = 1
    while w>z:
        z *= 2
    y = z-w
    x = t*(t-1)//2*g + z-1
    print(f"{g}*{a}/{t}+{d}={x}+{y}")