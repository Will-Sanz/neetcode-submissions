class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            max_reach = max(max_reach, i + nums[i])
            print(max_reach)
            if i == max_reach:
                return False
            if max_reach >= len(nums) - 1:
                return True
        return False