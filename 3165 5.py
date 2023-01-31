# 5
# Gold 3, 그리디 알고리즘

n,k = map(int,input().split())

def ten(j):
    n[j] = '0'
    while n[j-1] == '9':
            n[j-1] = '0'
            j -= 1
    n[j-1] = str(int(n[j-1])+1)

def check():
    if n.count('5') >= k:
        return True

n = list(str(n+1).zfill(16))
for i in range(15,0,-1):
    if n[i] == '10':
        ten(i)
    if check():break

    if n[i] >= '5':
        ten(i)
    if check():break

    n[i] = '5'

print(int(''.join(n)))