# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        n = length // k
        dummy = ListNode(0,head)
        curr = head
        p1 = dummy
        while n != 0:
            prev = None
            p2 = curr
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            p1.next = prev
            p2.next = curr
            p1 = p2
            n -= 1

        return dummy.next

