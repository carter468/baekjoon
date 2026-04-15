# 무한 수열
# Gold 5, DP

def f(x):
    if x in dic: return dic[x]

    dic[x] = f(x//P)+f(x//Q)
    return dic[x]

N,P,Q = map(int,input().split())

dic = {0:1}
print(f(N))