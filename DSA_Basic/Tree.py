# Tree
# Binary Tree Traversals
# A binary tree node is usually defined as:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Inorder Traversal (Left → Root → Right)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)
# Preorder Traversal (Root → Left → Right)
def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)
# Postorder Traversal (Left → Right → Root)
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end=" ")








# Level Order Traversal (BFS)
from collections import deque

def levelorder(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
# Build tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder:"); inorder(root); print()
print("Preorder:"); preorder(root); print()
print("Postorder:"); postorder(root); print()
print("Levelorder:"); levelorder(root); print()

# Inorder: 4 2 5 1 3
# Preorder: 1 2 4 5 3
# Postorder: 4 5 2 3 1
# Levelorder: 1 2 3 4 5



# Recursive traversals → Inorder, Preorder, Postorder.

# Iterative traversals → Using Stack (Inorder, Preorder, Postorder). (below)

# Level order traversal (BFS) → using Queue. (above program)


# Iterative Tree Traversals using Stack


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
# Iterative Inorder Traversal (Left → Root → Right)

def inorder(root):
    stack, res = [], []
    curr = root

    while curr or stack:
        # Go left as far as possible
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        res.append(curr.val)   # Visit root
        curr = curr.right      # Then go right

    return res

# 2️⃣ Iterative Preorder Traversal (Root → Left → Right)

def preorder(root):
    if not root:
        return []
    
    stack, res = [root], []

    while stack:
        node = stack.pop()
        res.append(node.val)

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return res


# 3️⃣ Iterative Postorder Traversal (Left → Right → Root)

# Method 1: Two Stacks


def postorder(root):
    if not root:
        return []

    stack1, stack2, res = [root], [], []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        res.append(stack2.pop().val)

    return res

# Method 2: One Stack (Trickier)

def postorder_one_stack(root):
    stack, res = [], []
    last_visited = None
    curr = root

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                last_visited = stack.pop()

    return res




