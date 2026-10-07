class Solution:
    def isPossible(self, target: list[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        pq = target
        heapq.heapify_max(pq)

        total_sum = sum(pq)
        while True:
            max_num = heapq.heappop_max(pq)

            if max_num == 1:
                return True

            rem_sum = total_sum - max_num
            if rem_sum == 1:
                return True
                
            new_num = max_num % rem_sum

            if new_num == max_num or new_num == 0:
                return False
            else:
                heapq.heappush_max(pq,new_num)
                total_sum = rem_sum + new_num

        


