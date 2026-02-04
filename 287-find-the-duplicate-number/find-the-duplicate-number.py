class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        n = len(nums)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        p1,p2 = 0,slow
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
            if p1 == p2:
                return p1
        return 0