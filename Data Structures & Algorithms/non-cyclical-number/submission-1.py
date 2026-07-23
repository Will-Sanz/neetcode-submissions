class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def square(n):
            ans = 0
            for c in str(n):
                ans += int(c) ** 2
            return ans
        
        while n > 0:
            n = square(n)
            if n == 1:
                return True
            if n in seen:
                return False
            else:
                seen.add(n)
        
            

            


        