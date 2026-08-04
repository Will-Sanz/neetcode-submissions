from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # make a map of the counts of the chars in s1
        # check that against a sliding window of s2
        s1counts = defaultdict(int)
        s2counts = defaultdict(int)
        for char in s1:
            s1counts[char] += 1
        left = 0
        for right in range(len(s2)):
            s2counts[s2[right]] += 1
            while right - left + 1 > len(s1):
                s2counts[s2[left]] -= 1
                # you have to delete 0 counts or else you could compare
                # {'a': 1} to {'a': 1, 'b': 0}
                if s2counts[s2[left]] == 0:
                    del s2counts[s2[left]]
                left += 1
            if s1counts == s2counts:
                return True
        return False