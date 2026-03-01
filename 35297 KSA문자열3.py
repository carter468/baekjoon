# KSA 문자열 3
# Gold 2, greedy

ksa = 'AKS'

X = list(input())

n = len(X)
while X:
    if X[-1] == ksa[n%3]:
        X.pop()
        n -= 1
    elif len(X) >= 2:
        X.pop()
        X.pop()
    else:
        break

print(n*2)