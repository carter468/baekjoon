# 목걸이 수열
# Gold 1, greedy

def check(w):
    for i in range(len(w)):
        if w[i:]+w[:i] < w:
            return False
    return True

S = input()

n = len(S)
i = 0
result = []
while i < n:
    for j in range(n,i,-1):
        if check(S[i:j]):
            result.append(S[i:j])
            i = j
            break

print(''.join(f'({f})' for f in result))