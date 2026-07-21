class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = defaultdict(int)
        for char in s:
            chars[char] += 1
        for char in t:
            chars[char] -= 1
        return all(v == 0 for v in chars.values())