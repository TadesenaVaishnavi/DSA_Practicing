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
