import sys
input = sys.stdin.readline

N = int(input())
tree = {}

for _ in range(N):
    x, y, z = input().strip().split()
    tree[x] = (y, z)

def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end="")
    inorder(tree[node][1])

def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")
print()
