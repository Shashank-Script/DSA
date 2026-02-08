class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nextIdx(curr):
            return (curr + nums[curr]) % n

        for i in range(n):
            isVisited = set()
            curr = i
            isPos = nums[i] > 0
            isVisited.add(curr)

            while True:
                nxt = nextIdx(curr)

                # direction change → invalid
                if isPos and nums[nxt] < 0:
                    break
                if not isPos and nums[nxt] > 0:
                    break

                # self-loop (length 1) → invalid
                if nxt == curr:
                    break

                # cycle found
                if nxt in isVisited:
                    return True

                isVisited.add(nxt)
                curr = nxt

        return False