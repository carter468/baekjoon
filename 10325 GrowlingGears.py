# Growling Gears
# Gold 5, math

for _ in range(int(input())):
    m = 0
    for i in range(int(input())):
        a,b,c = map(int,input().split())
        d = b/a/2
        e = -a*d*d+b*d+c
        if e > m:
            result = i+1
            m = e
    print(result)