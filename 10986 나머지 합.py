# 나머지 합
import sys
input = sys.stdin.readline
# n,m = 5,3
# arr = [1,2,3,1,2,0]   #1 3 6 7 9

n,m = map(int,input().split())
arr = list(map(int,input().split()))+[0]
sum_mod = [0]*m

for i in range(n):
    arr[i] = (arr[i]+arr[i-1]) % m  # 구간합을 m으로 나눈 나머지에 따라 리스트에 정리
    sum_mod[arr[i]] += 1     

ans = sum_mod[0]*(sum_mod[0]+1) //2
for i in range(1,m):
    ans += sum_mod[i]*(sum_mod[i]-1) //2
print(ans)
