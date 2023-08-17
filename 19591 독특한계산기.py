# 독특한 계산기
# Gold 3, deque, parsing

from collections import deque
P = {'+':0,'-':0,'*':1,'/':1}

def cal(a,b,c):
    if b == '+': return a+c
    if b == '-': return a-c
    if b == '*': return a*c
    if a > 0: return a//c if c > 0 else -(a//-c)
    return -(-a//c) if c > 0 else (-a//-c)

def parse():
    global l,r
    while r < len(S) and S[r].isdigit():
        r += 1
    q.append(int(S[l:r]))
    if r < len(S): q.append(S[r])
    r += 1
    l = r

S = input()
if S == '': exit()

q = deque()
if S[0] == '-':
    l,r = 0,1
    parse()
else: l,r = 0,0
while r < len(S):
    parse()

while len(q) > 1:
    a,b = P[q[1]],P[q[-2]]
    x,y = cal(q[0],q[1],q[2]),cal(q[-3],q[-2],q[-1])
    if a > b: z = 0
    elif a < b: z = 1
    else:
        if x < y: z = 1
        else: z = 0
    if z == 0:
        for _ in range(3): q.popleft()
        q.appendleft(x)
    else:
        for _ in range(3): q.pop()
        q.append(y)

print(q[0])