# 비즈네르 암호 해독
# Gold 5, bruteforcing

def check(i):
    for j in range(i):
        for k in range(N//i):
            if arr[k*i+j] != arr[j]: return False
    return True

A = input()
B = input()

N = len(A)
arr = []
for i in range(N):
    x = (ord(B[i])-ord(A[i]))%26
    if x == 0: x = 26
    arr.append(x)

f = set()
for i in range(1,int(N**0.5)+1):
    if N%i == 0:
        f.add(i)
        f.add(N//i)

for i in sorted(f):
    if check(i):
        print(''.join([chr(arr[j]+64) for j in range(i)]))
        break