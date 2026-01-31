class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr_sum(num):
            summ = 0
            while num > 0:
                dig = num % 10
                summ = summ + dig**2
                num //= 10
            return summ

        slow = fast = n
        while fast != 1:
            slow = sqr_sum(slow)
            fast = sqr_sum(sqr_sum(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
        return True