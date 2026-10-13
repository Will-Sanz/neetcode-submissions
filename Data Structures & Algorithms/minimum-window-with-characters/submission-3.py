class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = defaultdict(int)
        missing = len(t)
        if not t:
            return ""
        for c in t:
            check[c] += 1
        left = 0
        res = ""
        for right in range(len(s)):
            if s[right] in check:
                if check[s[right]] > 0:
                    missing -= 1
                check[s[right]] -= 1
            while missing == 0:
                if s[left] in t:
                    check[s[left]] += 1
                    if check[s[left]] > 0:
                        missing += 1
                if not res or right - left + 1 < len(res):
                    res = s[left: right + 1]
                left += 1
        return res

        
