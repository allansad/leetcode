# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 시간복잡도: 노드 개수에 대해 O(n)
        # 공간복잡도: 노드 개수에 대해 O(n)
        
        return_arr = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            return_arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return return_arr