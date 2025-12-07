# The End of the World
# Platinum 4, DP

def f(n,st,de,te):
    if n == 0:
        return 0
    
    p = S[n-1]
    if p == st:
        return f(n-1,st,te,de)
    elif p == de:
        return (1<<(n-1))+f(n-1,te,de,st)

while True:
    S = input()
    if S == 'X': break

    N = len(S)
    print((1<<N)-1-f(N,'A','B','C'))