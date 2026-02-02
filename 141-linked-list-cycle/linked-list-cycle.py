# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Method-1 : T.C = O(n) & S.C = O(n)
        # isVisited = set()
        # temp = head
        # while temp:
        #     if temp in isVisited:
        #         return True
        #     isVisited.add(temp)
        #     temp = temp.next
        # return False

        # Method-2 : T.C = O(n) & S.C = O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False