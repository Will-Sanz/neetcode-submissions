class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            seen[num] += 1
        for num in nums:
            temp = 1
            if num - 1 not in seen:
                while num + 1 in seen:
                    temp += 1
                    num += 1
                ans = max(ans, temp)
        return ans
                
            