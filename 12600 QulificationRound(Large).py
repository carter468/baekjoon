# Qulification Round (Large)
# Gold 1, ad hoc

for t in range(int(input())):
    _,C,*s = map(int,input().split())

    k = sum(s)//C
    while True:
        s = [min(k,x) for x in s]
        nk = sum(s)//C
        if nk == k:  
            break
        k = nk
    print(f'Case #{t+1}: {k}')