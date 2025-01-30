# Factor Solitaire
# Gold 2, greedy

n = int(input())

result = 0
while n > 1:
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            n,a = n-n//i,n//i
            result += n//a
            break
    else:
        n -= 1
        result += n
print(result)