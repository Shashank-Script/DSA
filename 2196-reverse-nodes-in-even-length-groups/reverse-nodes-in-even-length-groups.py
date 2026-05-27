# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        curr = head
        curr_prev = None
        size = 1
        while curr:
            if size > length:
                size = length
            
            if size % 2 != 0:
                for _ in range(size):
                    curr_prev = curr
                    curr = curr.next
            else:
                prev = None
                temp = curr
                for _ in range(size):
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                curr_prev.next = prev
                temp.next = curr
                curr_prev = temp
                
            length -= size
            size += 1
            
        return head

                