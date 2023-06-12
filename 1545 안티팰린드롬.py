# 안티 팰린드롬
# Gold 2, 그리디

def solve():
    s = sorted(input())
    n = len(s)
    l = n//2-1
    r = n//2+n%2
    while r < n:
        i = r
        while s[l] == s[i]:
            i += 1
            if i == n:
                return -1
        s[i],s[r] = s[r],s[i]
        l -= 1
        r += 1
    return ''.join(s)

print(solve())