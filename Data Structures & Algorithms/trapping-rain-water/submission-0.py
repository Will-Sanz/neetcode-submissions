class Solution:
    def trap(self, height: List[int]) -> int:
        # track the distance in between bars and the height
        ans = 0
        l, r = 0, len(height) - 1
        last = 0
        maxleft, maxright = height[0], height[len(height) - 1]
        while l <= r:
            maxleft = max(maxleft, height[l])
            maxright = max(maxright, height[r])
            if maxleft < maxright:
                toadd = (min(maxleft, maxright) - height[l])
                if toadd > 0:
                    ans += toadd
                l += 1
            else:
                toadd = (min(maxleft, maxright) - height[r])
                if toadd > 0:
                    ans += toadd
                r -= 1
        return ans

            
            


        