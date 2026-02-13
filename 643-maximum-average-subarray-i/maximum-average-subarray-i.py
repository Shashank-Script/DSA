class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = float('-inf')
        total = 0
        for i in range(k):
            total += nums[i]
        max_sum = max(total,max_sum)

        for i in range(k,len(nums)):
                total += nums[i]
                total -= nums[i-k]
                max_sum = max(total,max_sum)
                
        return max_sum / k