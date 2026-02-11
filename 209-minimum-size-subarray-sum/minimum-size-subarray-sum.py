class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        curr_sum = 0
        i = 0
        for j in range(len(nums)):
            curr_sum += nums[j]
            while curr_sum >= target:
                min_len = min(min_len, j-i+1)
                curr_sum -= nums[i]
                i += 1
                
        return 0 if min_len == float('inf') else min_len