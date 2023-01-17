import math

class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2
            hours = 0

            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                ans = min(ans, k)
                right = k - 1
            else:
                left = k + 1
        
        return ans