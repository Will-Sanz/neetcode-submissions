class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i], max_dp[i - 1] * nums[i])
            ans = max(ans, max_dp[i], min_dp[i])
        return ans
        