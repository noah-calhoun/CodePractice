# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.maxD = 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        # end found, bubble up and count
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    


def create_binary_search_tree(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    
    if val == None or val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

if __name__ == '__main__':
    root = [3,9,20,None,None,15,7]
    root = create_binary_search_tree(root)
    
    sol = Solution()
    inverted_root = sol.maxDepth(root)