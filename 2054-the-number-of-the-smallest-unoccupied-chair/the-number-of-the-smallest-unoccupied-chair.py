class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetFriArrive = times[targetFriend][0]

        times.sort(key = lambda x : x[0])
        
        freeChairs = []
        occupChairs = []

        for i in range(len(times)):
            heapq.heappush(freeChairs,i)
        
        for arrive,leave in times:
            while occupChairs:
                freeAt,chair = occupChairs[0]
                if arrive >= freeAt:
                    chairs = heapq.heappop(occupChairs)
                    heapq.heappush(freeChairs, chairs[1])
                else:
                    break
            
            freeChair = heapq.heappop(freeChairs)
            heapq.heappush(occupChairs,(leave,freeChair))
            if arrive == targetFriArrive:
                return freeChair
                    

            

            