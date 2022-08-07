# 트리 순회

N = int(input())            # 노드의 개수

tree = {}
for _ in range(N):
    a,b,c = map(str,input().split())
    tree[a] = [b,c]

def preorder(root):         # 전위순회
    if root != '.':
        print(root,end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):          # 중위순회
    if root != '.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])

def postorder(root):        # 후위순회
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()