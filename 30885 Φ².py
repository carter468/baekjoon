# Φ²
# Gold 4, simulation

n = int(input())
arr = tuple(map(int,input().split()))

prev = []
for i in range(n):
    prev.append((arr[i],i+1))

while len(prev) > 1:
    now = []
    i = 0
    while i < len(prev):
        a,b = prev[i]
        if i == 0:
            c = prev[i+1][0]
            if a >= c:
                now.append((a+c,b))
                i += 1
            else:
                now.append((a,b))
        elif i == len(prev)-1:
            c = now[-1][0]
            if a >= c:
                now.pop()
                now.append((a+c,b))
            else:
                now.append((a,b))
        else:
            c,d = now[-1][0],prev[i+1][0]
            if a < c and a < d:
                now.append((a,b))
            elif a < c and a >= d:
                now.append((a+d,b))
                i += 1
            elif a >= c and a < d:
                now.pop()
                now.append((a+c,b))
            elif a >= c and a >= d:
                now.pop()
                now.append((a+c+d,b))
                i += 1
        i += 1
    prev = now
print(prev[0][0])
print(prev[0][1])