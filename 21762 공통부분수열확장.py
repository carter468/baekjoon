# 공통 부분 수열 확장
# Platinum 4, greedy, prefix sum

def solve():
    def get_sten(s,w):
        n,m = len(s),len(w)
        st = [-1]*(m+1)
        en = [n]*(m+1)

        idx = 0
        for i in range(m):
            while s[idx] != w[i]:
                idx += 1
            st[i+1] = idx
            idx += 1

        idx = n-1
        for i in range(m-1,-1,-1):
            while s[idx] != w[i]:
                idx -= 1
            en[i] = idx
            idx -= 1

        return st,en

    def get_psum(s):
        psum = [[0]*26 for _ in range(len(s)+1)]
        for i,c in enumerate(s,1):
            psum[i] = psum[i-1][:]
            psum[i][ord(c)-97] += 1
        return psum
    
    def check(lx,rx,ly,ry):
        for c in range(26):
            if psumX[rx][c]-psumX[lx+1][c] > 0 and psumY[ry][c]-psumY[ly+1][c] > 0:
                return True
        return False

    X = input()
    Y = input()
    W = input()
    
    stX,enX = get_sten(X,W)
    stY,enY = get_sten(Y,W)

    psumX = get_psum(X)
    psumY = get_psum(Y)

    return 1 if any(check(*z) for z in zip(stX,enX,stY,enY)) else 0

for _ in range(int(input())):
    print(solve())