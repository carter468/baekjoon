# 캥거루 세마리 2

while True:
    try:
        a,b,c = map(int,input().split())
        x = max(b-a-1,c-b-1)
        print(x)
    except:
        break