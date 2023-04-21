# ZOAC
# Gold 5, 재귀

def sol(arr,idx):
    if not arr: return
    a = min(arr)
    i = arr.index(a)
    result[idx+i] = a
    print(''.join(result))
    sol(arr[i+1:],idx+i+1)
    sol(arr[:i],idx)

s = list(input())
result = ['']*len(s)
sol(s,0)