# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 시간복잡도: 노드 개수에 대해 O(n)
        # 공간복잡도: 노드 개수에 대해 O(n)

        if not root:
            return []
        queue = deque([root])
        result = [[root.val]]
        temp = deque()

        while queue:
            current = queue.popleft()
            if current.left:
                temp.append(current.left)
            if current.right:
                temp.append(current.right)

            if not queue:
                if temp:
                    result.append([n.val for n in temp])
                queue = temp
                temp = deque()

        return result
                    