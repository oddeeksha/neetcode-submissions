# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]      
    
        def max_height(root):
            if root is None:
                return 0
            left_max = max_height(root.left)
            right_max = max_height(root.right)
            largest_diameter[0] = max(largest_diameter[0], right_max+ left_max)
            return 1 + max(left_max, right_max)
        max_height(root)
        return largest_diameter[0]

            
            