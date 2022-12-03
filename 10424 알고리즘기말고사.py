# 알고리즘 기말고사
# Silver 2, 구현

n = int(input())
final_rank = list(map(int,input().split()))
answer = [0]*n
for i in range(n):
    answer[final_rank[i]-1] = final_rank[i]-i-1
for i in answer:
    print(i)