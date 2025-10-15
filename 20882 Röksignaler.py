# Röksignaler
# Gold 5, implementation

dic = dict()
for _ in range(26):
    x,y = input().split()
    dic[y] = x
S,P = map(int,input().split())
T,B,M = map(int,input().split())
N,signal = input().split()

result = []
c = ''
w = []
t = ''
for x in signal:
    if t == '':
        t = x
    elif t[0] == x:
        t += x
    else:
        if t[0] == '1':
            if len(t) == S:
                c += '-'
            elif len(t) == P:
                c += '.'
            t = x
        elif t[0] == '0':
            if len(t) == B:
                w.append(dic[c])
                c = ''
            elif len(t) == M:
                w.append(dic[c])
                c = ''
                result.append(''.join(w))
                w = []
            t = x

if len(t) == S:
    c += '-'
elif len(t) == P:
    c += '.'
w.append(dic[c])
result.append(''.join(w))

print(' '.join(result))