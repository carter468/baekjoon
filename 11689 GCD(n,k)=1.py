# GCD(n,k) = 1
# Gold 1, 오일러 피 함수

answer = n = int(input())
i = 2
p = 0
while i**2<=n:
    while n%i==0:
        n//=i
        if i!=p:
            answer*=(i-1)/i
            p=i
    i += 1
if n>1:
    answer*=(n-1)/n

print(int(answer))

# 소인수분해 결과포함
# def solve1(n):
#     answer = n
#     i = 2
#     factor = []
#     while i**2<=n:
#         while n%i==0:
#             factor.append(i)
#             n//=i
#         i += 1
#     if n>1:
#         factor.append(n)

#     for p in set(factor):
#         answer*=(p-1)/p

#     print(int(answer))

# 리스트 없이
# def solve2(n):
#     answer = n
#     i = 2
#     p = 0
#     while i**2<=n:
#         while n%i==0:
#             n//=i
#             if i!=p:
#                 answer*=(i-1)/i
#                 p=i
#         i += 1
#     if n>1:
#         answer*=(n-1)/n

#     print(int(answer))

# import time
# import random
# t1,t2 = 0,0
# for i in range(200):
#     n = random.randrange(1,10**12)

#     start_t = time.time()
#     solve1(n)
#     t1 += time.time() - start_t

#     start_t = time.time()
#     solve2(n)
#     t2 += time.time() - start_t
# print(t1,t2)