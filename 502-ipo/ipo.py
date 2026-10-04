class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = []
        max_profit = []

        for i in range(len(profits)):
            projects.append([capital[i],profits[i]])

        projects.sort(key=lambda x:x[0])

        ptr = 0
        for _ in range(k):
            while len(projects) > ptr:
                if w >= projects[ptr][0]:
                    heapq.heappush_max(max_profit,projects[ptr][1])
                    ptr += 1
                else:
                    break

            if not max_profit:
                return w
                
            w += heapq.heappop_max(max_profit)

        return w
            
