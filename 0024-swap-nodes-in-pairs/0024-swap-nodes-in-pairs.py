# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 시간복잡도: LinkedList의 노드 개수에 대해 O(n)
        # 공간복잡도: O(1)

        if not head or not head.next:
            return head

        temp = ListNode(0)
        temp.next = head
        prev = temp

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next= first
            prev.next = second

            prev = first

        return temp.next