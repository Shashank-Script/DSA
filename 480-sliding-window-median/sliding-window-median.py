class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        medians = []
        arr = nums[:k]
        arr.sort()
        if k % 2 == 0:
            med = (arr[(k//2) - 1] + arr[k//2]) / 2
            medians.append(med)
        else:
            med = arr[k//2]
            medians.append(med)

        for i in range(k,len(nums)):
            arr.append(nums[i])
            arr.remove(nums[i-k])
            arr.sort()
            if k % 2 == 0:
                med = (arr[(k//2) - 1] + arr[k//2]) / 2
                medians.append(med)
            else:
                med = arr[k//2]
                medians.append(med)
        
        return medians


