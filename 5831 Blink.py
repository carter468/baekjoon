# Blink
# Gold 3, bitmask, math

def answer(i):
    for j in range(n):
        print(i>>j&1)

n,b = map(int,input().split())

state = 0
for i in range(n):
    if input() == '1':
        state |= 1<<i

result = [-1]*(1<<n)
c = 0
while result[state] == -1:
    result[state] = c
    if c == b:
        answer(state)
        exit()
    c += 1
    nstate = state
    for i in range(n):
        if state>>((i-1)%n)&1:
            nstate ^= 1<<i
    state = nstate
x = (b-result[state])%(c-result[state])+result[state]
for i in range(1<<n):
    if result[i] == x:
        answer(i)