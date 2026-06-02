import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        odd,even = [],[]
        s = str(num)
        for c in s:
            n = int(c)
            if n % 2 == 0:
                heapq.heappush_max(even,n)
            else:
                heapq.heappush_max(odd,n)
        
        res = 0
        for c in s:
            n = int(c)
            if n % 2 == 0:
                dig = heapq.heappop_max(even)
            else:
                dig = heapq.heappop_max(odd)
            res = res * 10 + dig
        
        return res


