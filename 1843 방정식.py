# 방정식
# Gold 3, 수학

def restrict_A(n):
    return ((n-1)//2)**2 if n%2 else n*(n-2)//4

def restrict_B(n):
    divisor = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            divisor.append(i) 
            if i**2 != n: 
                divisor.append(n//i)
                
    divisor.sort()
    l = len(divisor)
    count = 0
    for i in range(l-1):
        for j in range(i,l-1):
            if divisor[i]+divisor[j] in divisor:
                count += 1
    return count

def restrict_C(n):
    seive = [True]*(n+1)
    for i in range(2,int(n**0.5)+1):
        if seive[i]:
            for j in range(i*i,n+1,i):
                seive[j] = False

    count = 0
    for i in range(3,n-1,2):
        if seive[i] and seive[i+2]:
            count += 1
    return count

N = int(input())
print(restrict_A(N))
print(restrict_B(N))
print(restrict_C(N))