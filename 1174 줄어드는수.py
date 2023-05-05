# 줄어드는 수
# Gold 5, 백트래킹

def bt(x):
    result.append(int(x))
    for i in range(int(x[-1])):
        bt(x+str(i))

result = []
for i in range(10):
    bt(str(i))

n = int(input())
print(sorted(result)[n-1] if n<1024 else -1)