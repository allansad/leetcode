# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 시간복잡도: linkedList의 길이에 대해 O(n)
        # 공간복잡도: linkedList의 길이에 대해 O(n)
        if not head:
            return head

        stack = []
        current = head
        
        while current:
            stack.append(current.val)
            current = current.next
        
        dummy = ListNode()
        current = dummy

        while len(stack) > 0:
            val = stack.pop()
            current.next = ListNode(val)
            current = current.next
            
        return dummy.next