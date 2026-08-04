class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # keeping track of the counts in a certain window
        counts = defaultdict(int)
        left = 0
        ans = 0
        for right in range(len(s)):
            # update the right count
            counts[s[right]] += 1
            # find the max count in the window
            maxcount = max(counts.values())
            # while window isn't valid, update counts, move left over
            while (right - left + 1) - maxcount > k:
                counts[s[left]] -= 1
                left += 1
            # update max length
            ans = max(ans, right - left + 1)
        return ans
        

            
        