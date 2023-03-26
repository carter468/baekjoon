# 문자 해독
# Gold 5, 슬라이딩 윈도우

g,s = map(int,input().split())
w = input()
S = input()

arr1 = [0]*58
for a in w:
    arr1[ord(a)-65] += 1

arr2 = [0]*58
for i in range(g):
    arr2[ord(S[i])-65] += 1
result = 1 if arr1==arr2 else 0
for i in range(s-g):
    arr2[ord(S[i])-65] -= 1
    arr2[ord(S[i+g])-65] += 1
    result += arr1==arr2

print(result)