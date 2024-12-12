# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 시간복잡도: 노드 수(n)에대해 O(n)
        # 공간복잡도: 트리의 높이(h)에 대해 O(h)
        def recursion(node, min_val, max_val):
            if not node:
                return True

            if (min_val is not None and node.val <= min_val):
                return False
            if (max_val is not None and node.val >= max_val):
                return False

            return recursion(node.left, min_val, node.val) and recursion(node.right, node.val, max_val)

        return recursion(root, None, None)