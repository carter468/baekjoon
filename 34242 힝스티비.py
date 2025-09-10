# 힝스티비
# Gold 5, bruteforcing

S = input()

n = len(S)
score = 0
for i in range(n-2):
    if S[i:i+3] == '+^+': score += 1
    elif S[i:i+3] == '-^-': score -= 1

m = 0
for i in range(n):
    c = 0

    s = S[max(0,i-2):min(n,i+3)]
    for j in range(len(s)-2):
        if s[j:j+3] == '+^+': c -= 1
        elif s[j:j+3] == '-^-': c += 1

    s = S[max(0,i-2):i]+S[i+1:min(n,i+3)]
    for j in range(len(s)-2):
        if s[j:j+3] == '+^+': c += 1
        elif s[j:j+3] == '-^-': c -= 1

    m = max(m,c)
    
print(score+m)