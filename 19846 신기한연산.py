# 신기한 연산
# Gold 1, ad hoc

N,M,Q = map(int,input().split())

result = ''
for i in range(M//2+1):
    result += chr(i%N+97)*2
print(result[:M])