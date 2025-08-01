# TREES - Easy

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path 
# such that adding up all the values along the path equals targetSum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == targetSum
        
        targetSum -= root.val
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))
