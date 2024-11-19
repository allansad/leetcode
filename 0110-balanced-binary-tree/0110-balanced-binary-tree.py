# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.calHeight(root) >= 0)
    def calHeight(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return 0
        
        left = self.calHeight(root.left)
        right = self.calHeight(root.right)

        if left < 0 or right < 0 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1