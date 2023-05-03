# 리모컨
# Gold 5, 브루트포스

def check(x):
    for i in x:
        if i in arr:
            return True
    return False

n = int(input())
m = int(input())
arr = tuple(input().split()) if m else []

answer = abs(n-100)
for i in range(0,10**6):
    x = str(i)
    if check(x): continue
    answer = min(answer,abs(n-i)+len(x))
    
print(answer)