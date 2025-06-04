# 대도시 구축
# Gold 3, ad hoc, greedy, case work

N,M = map(int,input().split())
arr = sorted([tuple(map(int,input().split())) for _ in range(M)])

result = N*(N+1)//2+(N-2)
if M == 2:
    a,b,c,d = *arr[0],*arr[1]
    if a == 1 and c == 1:
        for i in range(2,N+1):
            if i not in (b,d): break
        x,y,z = sorted((b,d,i))
        result += x*2+y+z-(b+d+2)
    elif a == 1:
        for i in range(2,N+1):
            if i != b and (min(i,b),max(i,b)) not in arr: break
        result += i-1
elif M == 1:
    a,b = arr[0]
    if a == 1:
        for i in range(2,N+1):
            if i != b: break
        result += i-1
print(result)