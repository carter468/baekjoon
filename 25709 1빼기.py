# 1 빼기
# Silver 3, 그리디알고리즘

n = input()
count = 0
while n:
    count += n.count('1')
    n = n.replace('1','')
    if not n or not int(n):
        break
    n = str(int(n)-1)
    count += 1
print(count)