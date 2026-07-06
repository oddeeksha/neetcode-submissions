# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if (root and not subRoot) or (not root and subRoot):
                return False
            return (root.val == subRoot.val) and sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        def checker(root, subRoot):
            if sameTree(root, subRoot):
                return True
            if root is None:
                return False
            return checker(root.left, subRoot) or checker(root.right, subRoot)
        return checker(root, subRoot)
        

        
        
        