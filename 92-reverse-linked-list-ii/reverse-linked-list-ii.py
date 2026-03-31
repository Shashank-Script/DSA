# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0,head)
        left_prev,left_node = dummy,head

        for _ in range(left-1):
            left_prev = left_node
            left_node = left_node.next
            
        prev,curr = None,left_node
        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        left_prev.next = prev
        left_node.next = curr

        return dummy.next


