class Node:
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        
def preorder(node):
    print(node.value, end="")
    if node.left != ".":
        preorder(node.left)
    if node.right != ".":
        preorder(node.right)

def inorder(node):
    if node.left != ".":
        inorder(node.left)
    print(node.value, end="")
    if node.right != ".":
        inorder(node.right)
    
def postorder(node):
    if node.left != ".":
        postorder(node.left)
    if node.right != ".":
        postorder(node.right)
    print(node.value, end="")

# 입력
import sys
input = sys.stdin.readline

n = int(input())
node_arr = []
for _ in range(n):
    info = input().split()
    node = Node(info[0],info[1], info[2])
    node_arr.append(node)
    
for na in node_arr:
    for n in node_arr:
        if n.left == na.value:
            n.left = na
        if n.right == na.value:
            n.right = na

preorder(node_arr[0])
print()
inorder(node_arr[0])
print()
postorder(node_arr[0])