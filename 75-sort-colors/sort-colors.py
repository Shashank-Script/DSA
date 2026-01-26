class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,k,j = 0,0,len(nums)-1

        while k <= j:
            if nums[k] == 1:
                k += 1
            elif nums[k] == 2:
                nums[k],nums[j] = nums[j],nums[k]
                j -= 1
            else:
                nums[i],nums[k] = nums[k],nums[i]
                i += 1
                k += 1
