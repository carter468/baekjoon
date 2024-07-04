# 팬케이크 뒤집기
# Gold 4, constructive

for _ in range(int(input())):
    n,*arr = map(int,input().split())
    result = []
    while n > 0:
        if arr[-1] == n:
            n -= 1
            arr.pop()
        elif arr[0] == n:
            result.append(n)
            n -= 1
            arr = arr[-1:0:-1]
        else:
            for i in range(n):
                if arr[i] == n:
                    arr = arr[-1:-n+i:-1]+arr[:i]
                    result.append(i+1)
                    result.append(n)
                    n -= 1
                    break
    print(len(result),*result)