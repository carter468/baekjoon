# 행운의 티켓
# Silver 4, 브루트포스

def solve():
    for i in range(len(s)//2,0,-1):
        for j in range(len(s)-i*2+1):
            if sum(s[j:j+i]) == sum(s[j+i:j+i*2]):
                return i*2
    return 0

s = list(map(int,input()))
print(solve())