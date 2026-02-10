class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        curr_sum = 0
        freq = {}

        if k > len(nums):
            return 0

        for i in range(k):
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0) + 1

        if len(freq) == k:
            max_sum = curr_sum

        for i in range(k,len(nums)):
            curr_sum += nums[i]
            freq[nums[i]] = freq.get(nums[i],0) + 1

            curr_sum -= nums[i-k]
            freq[nums[i-k]] -= 1
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]
            
            if len(freq) == k:
                max_sum = max(max_sum,curr_sum)

        return max_sum