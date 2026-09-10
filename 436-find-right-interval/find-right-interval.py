class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = n * [-1]

        min_start = []
        min_end = []

        for i in range(n):
            heapq.heappush(min_start,(intervals[i][0],i))
            heapq.heappush(min_end,(intervals[i][1],i))
            
        while min_start and min_end:
            start,start_idx = min_start[0]
            end,end_idx = min_end[0]

            if start >= end:
                heapq.heappop(min_end)
                res[end_idx] = start_idx
            else:
                heapq.heappop(min_start)
        
        return res
