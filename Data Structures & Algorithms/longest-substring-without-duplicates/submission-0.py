class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq = defaultdict(int)
        ans = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            



        