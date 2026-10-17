# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.left:
            if root.val == 0:
                return False
            if root.val == 1:
                return True

        if root.val == 2:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)
            return left or right
        else:
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)
            return left and right
            

            
            
