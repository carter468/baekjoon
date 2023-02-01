# 2487 섞기 수열
# Gold 4, 순열 사이클 분할

def LCM(a,b):
    c = a*b
    while b!=0:
        a,b = b,a%b
    return c//a

N = int(input())
array = list(map(int,input().split()))

result = 1
for i,j in enumerate(array):
    if j:
        count = 0
        while j:
            count += 1
            array[i] = 0
            i = j-1
            j = array[j-1]
        result = LCM(result,count)

print(result)

# def LCM(a,b):
#     c = a*b
#     while b!=0:
#         a,b = b,a%b
#     return c//a

# N = int(input())
# array = tuple(map(int,input().split()))

# visit = [False]*N
# result = 1
# for i,j in enumerate(array):
#     if not visit[i]:
#         cycle = []
#         while j not in cycle:
#             visit[j-1] = True
#             cycle.append(j)
#             j = array[j-1]
#         result = LCM(result,len(cycle))

# print(result)