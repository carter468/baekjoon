# 욘세이대학교
# Gold 5, greedy

N = int(input())
word = input()

x,y = 0,0
for i in range(N-1):
    if word[i] < word[i+1]: x += 1
    else: y += 1

if abs(x-y) < 2:
    print(N)
    print(word)
else:
    s = set(word)
    k = abs(x-y)-1
    arr = []
    if x > y:
        for i in range(25,-1,-1):
            c = chr(i+65)
            if c < word[-1] and c not in s:
                arr.append(c)
                s.add(c)
        if len(arr) < k:
            k += 2
            for i in range(25,-1,-1):
                c = chr(i+65)
                if c not in s:
                    arr.append(c)
    else:
        for i in range(26):
            c = chr(i+65)
            if c > word[-1] and c not in s:
                arr.append(c)
                s.add(c)
        if len(arr) < k:
            k += 2
            for i in range(26):
                c = chr(i+65)
                if c not in s:
                    arr.append(c)
    print(N+k)
    print(word+''.join(arr[:k]))