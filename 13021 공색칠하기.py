# 공 색칠하기
# Gold 5, ad hoc

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(m)]

result = [0]*(n+1)
for i in range(m):
    l,r = arr[i]
    for j in range(l,r+1):
        result[j] = i+1

count = set()
for r in result:
    count.add(r)
print(1<<len(count)-1)
