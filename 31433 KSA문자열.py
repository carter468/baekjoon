# KSA 문자열
# Gold 4, greedy

def solve(s,c):
    idx = 0
    for i in range(len(s)):
        if s[i] != 'KSA'[idx%3]: c += 1
        else: idx += 1
    return c+abs(len(x)-idx)

x = input()
print(min(solve(x,0),solve('K'+x,1),solve('KS'+x,2)))
