# 1,2,3 더하기

T = int(input())
ans = [0]*11
for i in range(1,11):
    for j in range(1,4):
        ans[i] += ans[i-j] 
        if i-j == 0 and i <= 3:
            ans[i] += 1
for _ in range(T):
    print(ans[int(input())])