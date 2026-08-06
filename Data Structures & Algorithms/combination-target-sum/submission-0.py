class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            # where we include the candidate
            dfs(i, curr, total + nums[i])
            # if we don't include it, clean up curr, don't include it in total, move i
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res