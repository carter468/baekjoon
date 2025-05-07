# Moons and Umbrellas
# Gold 5, DP

INF = 10**9

for t in range(int(input())):
    X,Y,S = input().split()
    X,Y = int(X),int(Y)
    
    c,j = 0,0
    if S[0] == 'C': j = INF
    elif S[0] == 'J': c = INF

    for s in S[1:]:
        c,j = min(c,j+Y),min(c+X,j)
        if s == 'C': j = INF
        elif s == 'J': c = INF
    print(f'Case #{t+1}: {min(c,j)}')