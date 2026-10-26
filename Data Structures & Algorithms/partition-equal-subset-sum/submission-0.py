class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # can I choose some numbers that sum to 1/2 total?
        # dp[k][s] = can I make sum s using only the first k numbers?
        n = len(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = True
        
        for k in range(1, n + 1):
            num = nums[k - 1]
            for s in range(target + 1):
                # skip, keep the previous rows answer
                dp[k][s] = dp[k - 1][s]
                # take, can earlier numbers supply the remainder?
                if s >= num:
                    dp[k][s] = dp[k][s] or dp[k - 1][s - num]
        
        return dp[n][target]

