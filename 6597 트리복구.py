# 트리 복구
# Gold 3, divide and conquer

def solve(root,s,e):
    if s > e: return
    for i in range(s,e):
        if preorder[root] == inorder[i]:
            solve(root+1,s,i)
            solve(root+1+(i-s),i+1,e)
            print(preorder[root],end='')

while True:
    try:
        preorder,inorder = input().split()
        solve(0,0,len(inorder))
        print()
    except: break