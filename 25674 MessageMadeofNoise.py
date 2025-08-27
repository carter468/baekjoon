# Message Made of Noise
# Gold 3, bitmask, ad hoc, number theory, probability

MOD = 150

def Alisa():
    s = ''
    for c in input():
        s += bin(ord(c)-96)[2:].zfill(5)
    s = s.ljust(150,'0')

    input()    
    arr = []
    for x in map(int,input().split()):
        if s[x%MOD] == '1':
            arr.append(x)
    print(len(arr))
    print(*arr)

def Eva():
    input()
    s = ['0']*75
    for x in map(int,input().split()):
        s[x%MOD] = '1'
    s = ''.join(s)

    result = ''
    for i in range(15):
        a = 0
        for j in range(5):
            if s[i*5+j] == '1': a += 1<<(4-j)
        if a == 0: break
        result += chr(a+96)
    print(result)

if input() == 'Alisa':
    Alisa()
else:
    Eva()