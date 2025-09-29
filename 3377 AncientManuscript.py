# Ancient Manuscript
# Gold 1, DP

def is_vowel(x): return x >= 21

def transition(i,c,p):
    e = 1 if c == p else 0

    if is_vowel(c) and is_vowel(p):
        for j in range(1,Vc):
            for k in range(1,Ve+1-e):
                if e:
                    dp[i][c][j+1][k+1] += dp[i-1][p][j][k]
                else:
                    dp[i][c][j+1][1] += dp[i-1][p][j][k]
    elif not is_vowel(c) and not is_vowel(p):
        for j in range(1,Cc):
            for k in range(1,Ce+1-e):
                if e:
                    dp[i][c][j+1][k+1] += dp[i-1][p][j][k]
                else:
                    dp[i][c][j+1][1] += dp[i-1][p][j][k]
    else:
        for j in range(1,(Vc if is_vowel(p) else Cc)+1):
            for k in range(1,(Ve if is_vowel(p) else Ce)+1):
                dp[i][c][1][1] += dp[i-1][p][j][k]

Ve,Vc,Ce,Cc = map(int,input().split())
S = input()

N = len(S)
arr = [chr(i) for i in range(ord('a'),ord('z')+1) if chr(i) not in 'aeiou']
arr.extend(list('aeiou'))
dic = {a:i for i,a in enumerate(arr)}

dp = [[[[0]*5 for _ in range(5)] for _ in range(26)] for _ in range(N)]
if S[0] == '*':
    for i in range(26):
        dp[0][i][1][1] = 1
else:
    dp[0][dic[S[0]]][1][1] = 1

for i in range(1,N):
    candidates = range(26) if S[i] == '*' else [dic[S[i]]]
    for c in candidates:
        for p in range(26):
            transition(i,c,p)

print(sum(dp[-1][c][j][k] for c in range(26) for j in range(5) for k in range(5))%(1<<64))