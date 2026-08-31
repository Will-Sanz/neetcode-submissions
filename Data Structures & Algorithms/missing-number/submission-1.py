class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        check = set()
        for num in nums:
            check.add(num)
        for num in range(len(nums)):
            if num not in check:
                return num
        return len(nums)

        