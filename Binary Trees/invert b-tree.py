from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # Swap the left and right subtrees recursively
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root

def create_binary_search_tree(values):
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    return root

def insert_into_bst(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

if __name__ == '__main__':
    root_values = [4, 2, 7, 1, 3, 6, 9]
    root = create_binary_search_tree(root_values)
    
    sol = Solution()
    inverted_root = sol.invertTree(root)
