# 소수 게임
# Gold 3, 소수, 우선순위 큐

import heapq
import sys
input = sys.stdin.readline

# 에라토스테네스 체
MAX = 5000001
seive = [1]*MAX
seive[0],seive[1] = 0,0
for i in range(2,int(MAX**0.5)+1):
    if seive[i]:
        for j in range(i*i,MAX,i):
            seive[j] = 0
score = 0
prime = [[],[]]

def get_score(num,player):  # 부른 숫자, 누구차례
    if seive[num] == 0: # 소수가 아닌 수
        if len(prime[not player]) == 3:
            return prime[not player][0]
        else:
            return 1000

    if seive[num] > 1:  # 불렀던 소수
        return 1000

    if seive[num] == 1: # 처음 나온 소수
        seive[num] += 1
        heapq.heappush(prime[player],num)
        if len(prime[player]) > 3:
            heapq.heappop(prime[player])
        return 0
    
for _ in range(int(input())):
    w,s = map(int,input().split())
    score -= get_score(w,0)
    score += get_score(s,1)

if score > 0:
    print('소수의 신 갓대웅')
elif score == 0:
    print('우열을 가릴 수 없음')
else:
    print('소수 마스터 갓규성')