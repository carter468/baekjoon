# 망가진 키보드
# Gold 5, two pointer

from collections import defaultdict

while m:=int(input()):
    s = input()
    result = 0
    dic = defaultdict(int)
    i,j = 0,0
    count = 0
    while j < len(s):
        dic[s[j]] += 1
        if dic[s[j]] == 1: count += 1
        if count <= m: result = max(result,j-i+1)
        else:
            while i <= j:
                i += 1
                dic[s[i-1]] -= 1
                if dic[s[i-1]] == 0:
                    count -= 1
                    break
        j += 1
    print(result)
