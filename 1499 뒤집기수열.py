# 뒤집기 수열
# Gold 1, DP

def dp(bi,bj,ai,aj,rev):
    state = (bi,bj,ai,aj,rev)
    if state in memo:
        return memo[state]
    if bi > bj: return 0
    
    m = 10**9
    
    if rev == 0:
        if B[bi] == A[ai]:
            m = min(m,dp(bi+1,bj,ai+1,aj,0))
        if B[bj] == A[aj]:
            m = min(m,dp(bi,bj-1,ai,aj-1,0))

        if B[bi] == A[aj]:
            m = min(m,dp(bi+1,bj,ai,aj-1,1)+1)
        if B[bj] == A[ai]:
            m = min(m,dp(bi,bj-1,ai+1,aj,1)+1)
    else:
        if B[bi] == A[aj]:
            m = min(m,dp(bi+1,bj,ai,aj-1,1))
        if B[bj] == A[ai]:
            m = min(m,dp(bi,bj-1,ai+1,aj,1))

        if B[bi] == A[ai]:
            m = min(m,dp(bi+1,bj,ai+1,aj,0)+1)
        if B[bj] == A[aj]:
            m = min(m,dp(bi,bj-1,ai,aj-1,0)+1)

    memo[(bi,bj,ai,aj,rev)] = m
    return m

A = input()
B = input()

N = len(A)
memo = dict()

result = dp(0,N-1,0,N-1,0)
print(result if result < 10**9 else -1)