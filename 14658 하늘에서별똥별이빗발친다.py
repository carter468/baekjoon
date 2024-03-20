# 하늘에서 별똥별이 빗발친다
# Gold 3, bruteforcing

n,m,l,k = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(k)]

result = 0
for x,_ in arr:
    for _,y in arr:
        c = 0
        for a,b in arr:
            if x <= a <= x+l and y <= b <= y+l: c += 1
        result = max(result,c)
print(k-result)