class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = defaultdict(list)
        ans = []
        for string in strs:
            temp = str(sorted(string))
            chars[temp].append(string)
        ans = list(chars.values())
        return ans