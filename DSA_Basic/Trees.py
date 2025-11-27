# 1) Height of Binary Tree

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# 2) Count Nodes in a Tree

def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
    
# 3) Count Leaf Nodes

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)

#  return 1 --> Then root node becomes the leaf node.

# 4) Check if Two Trees are Identical

def is_identical(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val and
            is_identical(root1.left, root2.left) and
            is_identical(root1.right, root2.right))

# 5) Mirror (Invert) a Binary Tree
# Example 1
Original Tree:              Mirrored Tree:
       4                           4
      / \                         / \
     2   7                       7   2
    / \ / \                     / \ / \
   1  3 6  9                   9  6 3  1

# Example 2
   2 --- Original Tree
  / \
 1   3
   2 --- Mirrored Tree:
  / \
 3   1

At root 2: swap → left=3, right=1
At node 3: no children → nothing
At node 1: no children → nothing

# 🛠️ Solution Approaches 1

def invertTree(root):
    if not root:
        return None
    
    # swap children
    root.left, root.right = root.right, root.left
    
    # recurse on children
    invertTree(root.left)
    invertTree(root.right)
    
    return root

# ⏱️ Time Complexity: O(N) (visit every node once)
# 📦 Space Complexity: O(H) (stack space, H = height of tree, worst case O(N) for skewed tree)

# method 2. Iterative (BFS with Queue)
# BFS --- level by level it traval

# Queue
# enqueue() → insert
# dequeue() → remove
# front() → see first element

# stack
# push() → insert
# pop() → remove
# peek() → see top element

#****
# deque
# A data structure where you can insert/remove from both ends (front and back).                

# Both are not same 
# Word	Meaning	Same?
# deque	- Double-ended queue data structure	❌ NO
# dequeue -	Operation to remove item from queue	❌ NO
                 
from collections import deque

def invertTreeIterative(root):
    if not root:
        return None
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        
        # swap children
        node.left, node.right = node.right, node.left
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# ⏱️ Time Complexity: O(N)
# 📦 Space Complexity: O(N) (queue can hold all nodes at worst level).


# New topic
# Binary Search Trees (BSTs)
         
# Create & Insert into BST
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 1) Insert into BST
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
# 2) Height of a Binary Tree
# in tree they is answer
         
# 3) Diameter of a Binary Tree
def diameter(root):
    def dfs(node):
        nonlocal max_diameter
        if not node:
            return 0
        
        # heights of left & right subtrees
        left_height = dfs(node.left)
        right_height = dfs(node.right)
        
        # diameter passing through this node
        max_diameter = max(max_diameter, left_height + right_height)
        
        return 1 + max(left_height, right_height)
    
    max_diameter = 0
    dfs(root)
    return max_diameter

                
       1
      / \
     2   3
    / \
   4   5
# Longest path = 4 → 2 → 1 → 3 (or 5 → 2 → 1 → 3)
# Diameter = 3 edges (or 4 nodes)

# 4) Lowest Common Ancestor (LCA)
                
def lca_bst(root, p, q):
    if not root:
        return None
    if p < root.val and q < root.val:
        return lca_bst(root.left, p, q)
    elif p > root.val and q > root.val:
        return lca_bst(root.right, p, q)
    else:
        return root
                    
# Case 2: In a General Binary Tree
# Here, we can’t use BST property.
def lca_binary_tree(root, p, q):
    if not root or root.val == p or root.val == q:
        return root
    
    left = lca_binary_tree(root.left, p, q)
    right = lca_binary_tree(root.right, p, q)
    
    if left and right:
        return root
    return left if left else right

