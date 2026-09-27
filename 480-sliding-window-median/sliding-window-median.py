class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        max_hp = []
        min_hp = []
        medians = []
        for i in range(k):
            if not max_hp:
                heapq.heappush_max(max_hp,nums[i])
                continue
            
            if len(max_hp) == len(min_hp):
                if nums[i] > max_hp[0]:
                    heapq.heappush(min_hp,nums[i])
                    heapq.heappush_max(max_hp,heapq.heappop(min_hp))
                else:
                    heapq.heappush_max(max_hp,nums[i])

            else:
                heapq.heappush_max(max_hp,nums[i])
                heapq.heappush(min_hp,heapq.heappop_max(max_hp))
            
        median = ((max_hp[0] + min_hp[0]) / 2) if k % 2 == 0 else max_hp[0]
        medians.append(median)

        removed = {}
        
        for i in range(k,len(nums)):
            counter = 0 
            add_num = nums[i]
            remove_num = nums[i-k]

            removed[remove_num] = removed.get(remove_num,0) + 1

            if add_num <= max_hp[0]:
                heapq.heappush_max(max_hp,add_num)
                counter += 1
            else:
                heapq.heappush(min_hp,add_num)
                counter -= 1
            
            if remove_num <= max_hp[0]:
                counter -= 1
            else:
                counter += 1

            if counter > 0:
                heapq.heappush(min_hp,heapq.heappop_max(max_hp))

            if counter < 0:
                heapq.heappush_max(max_hp,heapq.heappop(min_hp))

            while max_hp and max_hp[0] in removed:
                num = max_hp[0]
                heapq.heappop_max(max_hp)
                removed[num] -= 1
                if removed[num] == 0:
                    del removed[num]
            
            while min_hp and min_hp[0] in removed:
                num = min_hp[0]
                heapq.heappop(min_hp)
                removed[num] -= 1
                if removed[num] == 0:
                    del removed[num]
            
            median = ((max_hp[0] + min_hp[0]) / 2) if k % 2 == 0 else max_hp[0]
            medians.append(median)

        return medians


            
