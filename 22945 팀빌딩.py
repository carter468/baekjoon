# 팀 빌딩
# Gold 4, greedy

N = int(input())
arr = []
for i,x in enumerate(map(int,input().split())):
    arr.append((i,x))
arr.sort(key=lambda x:-x[1])

l = N
r = -1
result = 0
for i,x in arr:
    if l != N:
        result = max(result,x*(max(abs(l-i),abs(r-i))-1))
    l = min(l,i)
    r = max(r,i)
print(result)