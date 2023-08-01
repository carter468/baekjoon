# A와 B 2
# Gold 5, recursion

def dfs(t):
    if t == S:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])

S,T = input(),input()

dfs(T)
print(0) 