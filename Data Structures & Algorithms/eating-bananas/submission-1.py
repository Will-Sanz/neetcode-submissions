import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hour(x):
            ans = 0
            for num in piles:
                ans += math.ceil(num / x)
            return ans

        l, r = 1, max(piles)

        ans = r
        while l <= r:
            mid = (l + r) // 2
            hours = hour(mid)
            # need more hours, make value bigger
            if hours > h:
                l = mid + 1
            # finished in less hours, make value smaller
            else:
                ans = min(ans, mid)
                r = mid - 1
        return ans


        
        



        