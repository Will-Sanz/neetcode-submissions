import heapq

class KthLargest:
    # add to the min heap until you reach k elements
    # compare the newest value to the root, if it's larger, you add,
    # if it's smaller you discard

    def __init__(self, k: int, nums: List[int]):
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        

        

        
