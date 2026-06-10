import heapq
class MedianFinder:

    def __init__(self):
        self.max_pq,self.min_pq = [],[]
        
    def addNum(self, num: int) -> None:
        max_pq,min_pq = self.max_pq,self.min_pq

        if len(max_pq) == 0:
            heapq.heappush_max(max_pq,num)
            return

        if len(max_pq) == len(min_pq):
            if num > max_pq[0]:
                heapq.heappush(min_pq,num)
                heapq.heappush_max(max_pq,heapq.heappop(min_pq))
            else:
                heapq.heappush_max(max_pq,num)

        else:
            heapq.heappush_max(max_pq,num)
            heapq.heappush(min_pq, heapq.heappop_max(max_pq))
        

    def findMedian(self) -> float:
        max_pq,min_pq = self.max_pq,self.min_pq

        if len(max_pq) == len(min_pq):
            m1 = max_pq[0]
            m2 = min_pq[0]
            return (m1+m2) / 2
        else:
            return max_pq[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()