class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            maxcount = max(counts.values())
            while (right - left + 1) - maxcount > k:
                counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        

            
        