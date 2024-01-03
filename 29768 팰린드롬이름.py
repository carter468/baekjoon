# 팰린드롬 이름
# Gold 5, ad hoc, constructive

n,k = map(int,input().split())
print('a'*(n-k)+'abcdefghijklmnopqrstuvwxyz'[:k])