# 최댓값

max_value = 0
answer = [1,1]
for i in range(1,10):
    numbers = [0]+list(map(int,input().split()))
    for j in range(1,10):
        if numbers[j] > max_value:
            max_value = numbers[j]
            answer = [i,j]
print(max_value)
print(*answer)