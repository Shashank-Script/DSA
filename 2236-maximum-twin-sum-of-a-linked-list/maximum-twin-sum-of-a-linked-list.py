# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr,prev = slow,None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 
        
        maxi = float('-inf')
        ptr1,ptr2 = head,prev
        while ptr1 and ptr2:
            summ = ptr1.val + ptr2.val
            maxi = max(summ,maxi)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return maxi
        
        