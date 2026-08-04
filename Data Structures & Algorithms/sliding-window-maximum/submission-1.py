class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque() # contains indices
        l = r = 0

        while r < len(nums):
            # while the queue has numbers and there are smaller numbers
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)

            # remove the left value if out of bounds
            if l > queue[0]:
                queue.popleft()

            if (r + 1) >= k:
                ans.append(nums[queue[0]])
                l += 1
            r += 1
        return ans