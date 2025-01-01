# 나는 건포도가 싫어요
# Gold 5, greedy, ad hoc

X,Y,Z = map(int,input().split())

a = min(X,Y,Z)
if X == Y == Z == 3 or a < 3: print(0)
else: print((a+1)//2-1)