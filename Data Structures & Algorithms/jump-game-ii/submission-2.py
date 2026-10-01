class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        curr_end = 0
        count = 0
        for i in range(len(nums) - 1):
            max_reach = max(max_reach, nums[i] + i)
            if i == curr_end:
                count += 1
                curr_end = max_reach
        return count