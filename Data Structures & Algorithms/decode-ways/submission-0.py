class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = the number of ways to decode the i characters we've seen
        # "What could my last decoded letter be?"
        # if the last digit is valid, dp[i] += dp[i - 1]
        # if the last digit isn't valid dp[i] += dp[i - 2]

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        # for each i, ask about the last decision
        for i in range(1, len(s) + 1):
            if 0 < int(s[i - 1]) < 10: 
                dp[i] += dp[i - 1]
            if i >= 2 and 9 < int(s[i - 2: i]) < 27:
                dp[i] += dp[i - 2]
        return dp[-1]