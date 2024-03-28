# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # The primary condition the root was checking with the given input values
        if not root or root==p or root==q:
            return root
        # Now recursively call the function that will match the exact values
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        # If both are matched return root or which was having minimum value return it
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
        