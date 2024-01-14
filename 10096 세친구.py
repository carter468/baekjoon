# 세 친구
# Gold 3, ad hoc, string

def solve():
    n = int(input())
    s = input()

    if n%2 == 0: return 'NOT POSSIBLE'
    n //= 2
    if len(set(s)) == 1: return s[:n]
    if s[:n] == s[n:-1] and s[1:n+1] == s[n+1:]: return 'NOT UNIQUE'

    for i in range(n):
        if s[i] != s[i+n+1]:
            if s[i+1:n+1] == s[i+n+1:]: return s[n+1:]
            else: break
    else: return s[:n]

    for i in range(n):
        if s[i] != s[i+n]:
            if s[i:n] == s[i+n+1:]: return s[:n]
            else: return 'NOT POSSIBLE'
    else: return s[:n]

print(solve())