# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev,curr = None,slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        p1,p2 = head,prev
        while p2.next:
            p1_next = p1.next
            p1.next = p2
            p1 = p1_next
            p2_next = p2.next
            p2.next = p1
            p2 = p2_next

        