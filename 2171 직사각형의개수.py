# 직사각형의 개수
# Gold 5, bruteforcing

p = set([tuple(map(int,input().split())) for _ in range(int(input()))])

count = 0
for x1,y1 in p:
    for x2,y2 in p:
        if x1 != x2 and y1 != y2 and (x2,y1) in p and (x1,y2) in p:
            count += 1
print(count//4)