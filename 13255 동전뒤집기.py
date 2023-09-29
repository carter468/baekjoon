# 동전 뒤집기
# Gold 3, probability, linearity of expectation, DP

n,k = int(input()),int(input())

odd,even = 0,1
for a in map(int,input().split()):
    odd,even = odd*(n-a)+even*a,odd*a+even*(n-a)
print(even/n**(k-1))