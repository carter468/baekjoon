# 징검다리 게임
# Gold 2, implementation, case work, prefix sum

N = int(input())
A = tuple(map(int,input().split()))
K = int(input())
S = input()

def f(arr):
    result = [10**9]*K
    if not arr: return result
    for i in range(len(arr)-1):
        a,b = arr[i],arr[i+1]
        for j in range(a+1,b+1):
            result[j] = b
    for j in range(arr[0]+1):
        result[j] = arr[0]
    for j in range(arr[-1]+1,K):
        result[j] = arr[0]
    return result

def e(): exit(print('NO'))

def g(a,b):
    if a <= b: return count[b]-count[a-1]
    else: return count[-2]-(count[a-1]-count[b])

jump,attack,delete = [],[],[]
count = [0]*(K+1)
for i in range(K):
    if S[i] == 'J': jump.append(i)
    elif S[i] == 'A': 
        attack.append(i)
        count[i] = 1
    else: delete.append(i)
    count[i] += count[i-1]

if not jump: e()
jump,attack,delete = f(jump),f(attack),f(delete)

i = 0
for x in A[1:-1]:
    if x == 0: i = (jump[i]+1)%K
    elif x == -1:
        d = delete[i]
        if d < i: d += K
        if d == 10**9: e()

        a = attack[i]
        if a < i: a += K

        j = jump[i]
        if j < i: j += K

        if d < j and d < a: i = (j+1)%K
        else: e()
    else:
        j = jump[i]
        if g(i,j) >= x: i = (j+1)%K
        else: e()
print('YES')