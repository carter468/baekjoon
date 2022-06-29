#가장 긴 바이토닉 부분수열

n = 10
seq = [1, 5, 2, 1, 4 ,3 ,4 ,5 ,2, 1]

n = int(input())
seq = list(map(int,input().split()))
forw = [1]*n #forward
backw = [1]*n   #backward

# 정방향 LIS 길이
for i in range(n):
    for j in range(i):
        if seq[j] < seq[i]:         
            forw[i] = max(forw[i],forw[j]+1)

# 역방향 LIS 길이
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if seq[j] < seq[i]:         
            backw[i] = max(backw[i],backw[j]+1)

# 바이토닉 부분수열 길이
max_len = 0
for i in range(n):
    max_len = max(max_len,forw[i]+backw[i]-1)
print(max_len)