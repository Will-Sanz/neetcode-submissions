class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        count = 0
        # if there is overlap, delete the one that ends later
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            # overlap
            if start < last_end:
                res[-1][1] = min(last_end, end)
                count += 1
            else:
                res.append([start, end])
        return count
