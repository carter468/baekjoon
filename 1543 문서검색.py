# 문서 검색
# Silver 4, 브루트포스 알고리즘

doc = input()
word = input()
n = len(word)
count = 0
idx = 0
while idx<=len(doc)-n:
    if doc[idx:idx+n] == word:
        count += 1
        idx += n
    else:
        idx += 1
print(count)