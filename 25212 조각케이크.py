# 조각 케이크
# Silver 2, 브루트포스 알고리즘

def merge(total,idx):
    global answer
    if 0.99<=total<=1.01:
        answer += 1
    for i in range(idx,n):
        merge(total+1/piece_cake[i],i+1)

n = int(input())
piece_cake = tuple(map(int,input().split()))
answer = 0 
merge(0,0)
print(answer)