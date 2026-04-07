# 울타리
# Platinum 5, bruteforcing, greedy

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

result = N
for i in range(N):
    for j in range(N):
        for k in range(N):
            for m in range(N):
                a,b,c,d = arr[i][0],arr[j][0],arr[k][1],arr[m][1]
                if a > b: a,b = b,a
                if c > d: c,d = d,c
                t = (b+d-a-c)*2
                count = 0
                length = []
                for x,y,l in arr:
                    if a < x < b and c < y < d:
                        length.append(l)
                    elif x < a or x > b or y < c or y > d:
                        t -= l
                        count += 1
                length.sort()
                while length and t > 0:
                    t -= length.pop()
                    count += 1
                if t <= 0: result = min(result,count)
print(result)