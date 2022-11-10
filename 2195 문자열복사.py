# 문자열 복사

s = input()
p = input()

l = len(s)
count = 0
while p:
    l = min(l,len(p))
    for i in range(l,0,-1):
        if p[:i] in s:
            count += 1
            p = p[i:]
            break
print(count)