class TimeMap:

    # (key, [value, timestamp]) -> binary search timestamps
    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.store[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return self.store[key][right][0] if right != -1 else ""