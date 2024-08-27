# 전생했더니 슬라임 연구자였던 건에 대하여 (Easy)
# Gold 5, math

k = int(input())

count = 0
for i in range(2,int(k**0.5)+1):
    while k%i == 0:
        k //= i
        count += 1
if k > 1: count += 1

result = 0
while count > 2**result:
    result += 1
print(result)
