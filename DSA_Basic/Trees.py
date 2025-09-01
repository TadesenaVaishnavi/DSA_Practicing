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

# 2. Iterative (BFS with Queue)

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
