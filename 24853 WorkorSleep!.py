# Work or Sleep!
# Gold 5, math

X,T = map(int,input().split())

if X == 100:
    print(500*T/6)
else:
    a = min(max((7-X/(100-X))*T/12,T/6),T/3)
    print((X+(a*6/T-1)*(100-X))*(T-a))