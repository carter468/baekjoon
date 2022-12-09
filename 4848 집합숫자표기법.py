# 집합 숫자 표기법
# Silver 2, 다이나믹 프로그래밍, 해시, 문자열

import sys
input = sys.stdin.readline

# 0~15 집합숫자표기와 그 길이
setnum = ['{}','{{}}']
length = {2:0,4:1}
for i in range(2,16):
    setnum.append(setnum[i-1][:-1]+','+setnum[i-1]+'}')
    length[len(setnum[i])] = i

for _ in range(int(input())):
    a = length[len(input().strip())]
    b = length[len(input().strip())]
    print(setnum[a+b])