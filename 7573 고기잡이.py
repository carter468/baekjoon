# 고기잡이
# Gold 3, bruteforcing

N,l,M = map(int,input().split())
fish = [tuple(map(int,input().split())) for _ in range(M)]

result = 0
for x,_ in fish:
    for _,y in fish:
        for k in range(1,l//2):
            nx = x+k
            ny = y+l//2-k
            count = 0
            for a,b in fish:
                if x <= a <= nx and y <= b <= ny: count += 1
            result = max(result,count)
print(result)