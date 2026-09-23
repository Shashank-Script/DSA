class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_cnt = {}
        res = []
        for task in tasks:
            task_cnt[task] = task_cnt.get(task,0) + 1
        
        task_pq = []
        cooldown = deque()
        for key,value in task_cnt.items():
            heapq.heappush_max(task_pq,(value,0,key))
        
        time = 0
        while task_pq or cooldown:
            while cooldown and time >= cooldown[0][1]:
                freq,exe_time,task = cooldown.popleft()
                heapq.heappush_max(task_pq,(freq,exe_time,task))
            
            if task_pq:
                freq,exe_time,task = heapq.heappop_max(task_pq)
                freq -= 1
                exe_time = time + n + 1
                if freq != 0:
                    cooldown.append((freq,exe_time,task))
            
            time += 1
        
        return time
            


