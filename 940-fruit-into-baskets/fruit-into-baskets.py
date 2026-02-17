class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = float('-inf')
        basket = {}
        i = 0
        for j in range(len(fruits)):
            basket[fruits[j]] = basket.get(fruits[j],0) + 1

            while len(basket) > 2:
                basket[fruits[i]] -= 1
                if basket[fruits[i]] == 0:
                    del basket[fruits[i]]
                i += 1

            max_fruit = max(j-i+1,max_fruit)
            
        return max_fruit

        