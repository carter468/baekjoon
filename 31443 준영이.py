# 준영이
# Gold 4, greedy, ad hoc

n,m = map(int,input().split())

if n < 3 and m < 3: 
    print(n*m)
else:
    a,b = divmod(n*m,3)
    if b == 0:
        c = 1
    elif b == 1:
        c = 4
        a -= 1
    elif b == 2:
        c = 2
    print(3**max(0,a)*c%(10**9+7))