# 너의 티어는?

def fac(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res

w,l,d = map(float,input().split())
tier = [0,0,0,0,0]      # 브 실 골 플 다
for i in range(21):     # 승
    for j in range(21-i): # 무
        p = 2000+50*(2*i+j-20)
        if p<1500:
            tier[0] += fac(20)/fac(i)/fac(20-i-j)/fac(j)*(w**i)*(l**(20-i-j))*(d**j)
        elif p<2000:
            tier[1] += fac(20)/fac(i)/fac(20-i-j)/fac(j)*(w**i)*(l**(20-i-j))*(d**j)
        elif p<2500:
            tier[2] += fac(20)/fac(i)/fac(20-i-j)/fac(j)*(w**i)*(l**(20-i-j))*(d**j)
        elif p<3000:
            tier[3] += fac(20)/fac(i)/fac(20-i-j)/fac(j)*(w**i)*(l**(20-i-j))*(d**j)
        else:
            tier[4] += fac(20)/fac(i)/fac(20-i-j)/fac(j)*(w**i)*(l**(20-i-j))*(d**j)
for i in tier:
    print(f'{i:.8f}')