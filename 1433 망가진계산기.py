# 망가진 계산기
# Gold 1, 백트래킹

def bt(n,cnt):
    global result

    if (n,cnt) in s or n >= 10**D:
        return
    s.add((n,cnt))

    if cnt == P:
        result = max(result,n)
        return

    for i in range(2,10):
        bt(n*i,cnt+1)

D,P = map(int,input().split())

s = set()
result = -1
bt(1,0)

print(result)