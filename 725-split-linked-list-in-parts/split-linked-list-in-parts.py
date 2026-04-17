# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        size = length // k
        extra = length % k
        res = []

        curr,prev = head,None 

        for i in range(k):
            count = size
            if extra > 0:
                count += 1
                extra -= 1
            
            subHead = curr
            for _ in range(count):
                prev = curr
                curr = curr.next

            if prev:    
                prev.next = None
            res.append(subHead)

        return res


