class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] represents the min cost to get to stair i

        n = len(cost)
        dp = [0] * n

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 2], dp[i - 1])
        
        return min(dp[-1], dp[-2])