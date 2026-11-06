class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            sum_h = 0
            for pile in piles:
                sum_h += self.ceil(pile, mid_k)
            if sum_h <= h:
                max_k = mid_k
            else:
                min_k = mid_k + 1
        return max_k if min_k == max_k else - 1
        
    def ceil(self, x: int, k: int) -> int:
        if k == 0:
            raise ZeroDivisionError("k cannot be 0")
        # For positive x and k:
        return (x + k - 1) // k
        
        