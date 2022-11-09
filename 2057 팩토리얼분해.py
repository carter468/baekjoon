# 팩토리얼 분해

MAX = 10**18

# MAX 이하의 팩토리얼 값 리스트
factorial = [1]
i = 1
while True:
    a = factorial[-1]*i
    if a>MAX:
        break
    factorial.append(a)
    i += 1

# dfs를 이용한 조합 찾기
def solve(num,total):
    if total>n:
        return 
    if total==n:
        print('YES')
        quit()
    for i in range(num,20):
        if not visit[i]:
            visit[i] = True
            solve(i,total+factorial[i])
            visit[i] = False

n = int(input())
visit = [False]*20
if n:
    solve(0,0)
print('NO')