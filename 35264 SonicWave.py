# Sonic Wave
# Gold 4, greedy, prefix sum, constructive

input()
Y = tuple(map(int,input().split()))

result = []
arr = [0]*4
for i,y in enumerate(Y):
    y -= arr[i%4]
    if y > 0:
        result.append((i+1,y,3))
        arr[i%4] += y
        arr[(i+2)%4] -= y
    elif y < 0:
        result.append((i+1,-y,1))
        arr[i%4] += y
        arr[(i+2)%4] -= y

print(len(result))
if result:
    for r in result: print(*r)