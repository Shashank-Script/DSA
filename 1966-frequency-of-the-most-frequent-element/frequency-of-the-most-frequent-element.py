class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 0
        Sum = 0
        i = 0
        for j in range(len(nums)):
            Sum += nums[j]
            while (j - i + 1) * nums[j] - Sum > k:
                Sum -= nums[i]
                i += 1
            max_freq = max(j - i + 1,max_freq)
        return max_freq


        


        