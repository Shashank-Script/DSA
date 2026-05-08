# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0,head)
        
        prev,curr1 = dummy,head

        while curr1 != None and curr1.next != None:
            curr2 = curr1.next
            prev.next = curr2
            curr1.next = curr2.next
            curr2.next = curr1
            prev = curr1
            curr1 = curr1.next
            
        return dummy.next
