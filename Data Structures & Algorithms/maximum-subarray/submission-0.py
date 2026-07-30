class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_here = 0
        max_so_far = nums[0]
        for num in nums:
            if max_here < 0:
                max_here = 0
            max_here += num
            max_so_far = max(max_so_far, max_here)
        return max_so_far
        