n=int(input())
tree={}
for i in range(n):
    node,left,right = input().split()
    tree[node]=[left,right]

def preorder(node):
    print(node, end="")
    left=tree[node][0]
    right=tree[node][1]
    if left != '.':
        preorder(left)
    if right != ".":
        preorder(right)


def inorder(node):
    left=tree[node][0]
    right=tree[node][1]
    if left != ".":
        inorder(left)
    print(node, end="")
    if right != ".":
        inorder(right)

def postorder(node):
    left=tree[node][0]
    right=tree[node][1]
    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(node, end="")


preorder("*")
print()
inorder("*")
print()
postorder("*")
