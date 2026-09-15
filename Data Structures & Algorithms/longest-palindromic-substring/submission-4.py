class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        res = ''

        if len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        for i in range(len(s)):
            # even length
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > ans:
                    res = s[left: right + 1]
                    ans = max(ans, right - left + 1)
                left -= 1
                right += 1

            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > ans:
                    res = s[left: right + 1]
                    ans = max(ans, right - left + 1)
                left -= 1
                right += 1
        
        return res


                
