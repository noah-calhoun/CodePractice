

import math
from typing import Optional



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = [0]

        def dfs(root):

            if root == None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            height[0] = max(height[0], 2 + left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return height[0]





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
    root = [1,2,3,4,5]
    root = create_binary_search_tree(root)
    
    sol = Solution()
    inverted_root = sol.diameterOfBinaryTree(root)