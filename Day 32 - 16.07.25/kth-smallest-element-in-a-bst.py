# TREES - Medium

# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            elements.append(node.val)
            if node.right:
                inorder(node.right)
        
        inorder(root)
        return elements[k-1]
