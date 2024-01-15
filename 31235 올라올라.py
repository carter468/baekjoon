# 올라올라
# Gold 4, ad hoc

n = input()
arr = tuple(map(int,input().split()))

result = 0
c = 1
a = arr[0]
for x in arr[1:]:
    if x >= a:
        result = max(result,c)
        c = 0
        a = x
    c += 1
result = max(result,c)
print(result if result else n)