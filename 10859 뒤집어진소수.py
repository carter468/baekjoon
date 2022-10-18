# 뒤집어진 소수

n = input()

def solve(n):
    def prime(x):
        if x==1:
            return False
        for i in range(2,int(x**0.5)+1):
            if x%i == 0:
                return False
        return True

    if prime(int(n)) == False:
        return 'no'
    if '3' in n or '4' in n or '7' in n:
        return 'no'
    m = ''
    for i in range(len(n)-1,-1,-1):
        if n[i] == '6':
            m += '9'
        elif n[i] == '9':
            m += '6'
        else:
            m += n[i]
    if prime(int(m)) == False:
        return 'no'
    return 'yes'

print(solve(n))