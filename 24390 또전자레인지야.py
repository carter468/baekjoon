# 또 전자 레인지야?
# Silver 1, 그리디 알고리즘

min,sec = map(int,input().split(':'))

if min+sec == 0:
    print(0)
elif sec<30:
    print(min//10+min%10+sec//10+1)
else:
    print(min//10+min%10+(sec-30)//10+1)