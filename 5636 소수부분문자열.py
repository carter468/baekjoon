# 소수 부분 문자열
# Silver 1, 소수판정, 문자열

import sys
input = sys.stdin.readline

MAX = 100000
seive = [True]*MAX
seive[0],seive[1] = False,False
for i in range(2,int(MAX**0.5)+1):
    if seive[i]:
        for j in range(i*i,MAX,i):
            seive[j] = False

while 1:
    s = input().strip()
    if s=='0':
        break

    l = len(s)
    m = min(5,l)
    prime = 0
    for i in range(m,0,-1):
        for j in range(l-m+1):
            c = int(s[j:j+i])
            if seive[c]:
                prime = max(prime,c)
        if prime:
            print(prime)
            break
    else:
        print()

# import sys
# input = sys.stdin.readline

# def is_prime(x):
#     if x==0 or x==1:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True

# while 1:
#     s = input().strip()
#     if s=='0':
#         break

#     l = len(s)
#     m = min(5,l)
#     prime = 0
#     for i in range(m,0,-1):
#         for j in range(l-m+1):
#             c = int(s[j:j+i])
#             if is_prime(c):
#                 prime = max(prime,c)
#         if prime:
#             print(prime)
#             break
#     else:
#         print()