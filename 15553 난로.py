# 15553 난로
# Gold 5, 그리디알고리즘

import sys
input = sys.stdin.readline

n,k = map(int,input().split())

# 방문시간을 입력받으면서 다음 사람까지의 텀을 저장
time = [int(input())]
term = []
for _ in range(n-1):
    time.append(int(input()))
    term.append(time[-1]-time[-2]-1)

# n번 켤 수 있으면 n초만 켜져있으면 되고, 
# k번 켤 수 있으면 n-k번의 텀만큼 추가로 켜져있어야한다.
# n-k개의 작은 텀을 선택하면 된다.
term.sort()
print(n+sum(term[:n-k]))
# term.sort(reverse=True)
# answer = n
# for _ in range(n-k):
#     answer += term.pop()
# print(answer)