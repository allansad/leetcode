# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 시간복잡도: 전체 링크드 리스트를 one_step와 two_step가 한번씩 순회하므로 노드 수에 대해 O(n)
        # 공간복잡도: O(1)
        

        one_step = head
        two_step = head
        while one_step and two_step.next:
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step == two_step:
                return True
            if not hasattr(two_step, "next"):
                return False
        return False
        