class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_here = 0
        max_so_far = nums[0]
        for num in nums:
            # we never want a negative prefix
            if max_here < 0:
                max_here = 0
            # add to the max here
            max_here += num
            # compare to overall max
            max_so_far = max(max_so_far, max_here)
        return max_so_far
        