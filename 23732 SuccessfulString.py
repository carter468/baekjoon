# Successful String
# Gold 5, combinatorics

N = int(input())
S = input()

result = 0
j = -1
for i in range(N-1):
    if S[i] == S[i+1]:
        result += (i-j)*(N-i-1)
        j = i
print(result)