# 새 앨범
# Gold 5, math

n,l,c = int(input()),int(input()),int(input())

a = (c+1)//(l+1)
if a%13 == 0:
    a -= 1

result = n//a
n %= a

if n > 0:
    result += 1
    if n%13 == 0 and (n == a-1 or result == 1):
        result += 1

print(result)