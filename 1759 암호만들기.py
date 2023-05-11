# 암호 만들기
# Gold 5, 백트래킹

def check(s):
    a = 0
    for c in s:
        a += c in ('a','e','i','o','u')
    return a > 0 and l-a > 1

def bt(result,count):
    if count == l and check(result):
        print(result)
        return
    for a in arr:
        if not result or result[-1] < a:
            bt(result+a,count+1)

l,_ = map(int,input().split())
arr = sorted(input().split())
bt('',0)