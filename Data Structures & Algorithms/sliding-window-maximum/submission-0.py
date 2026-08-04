class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        for right in range(k - 1, len(nums)):
            while right - left + 1 > k:
                left += 1
            ans.append(max(nums[left: right + 1]))
        return ans