import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative = []
        for stone in stones:
            negative.append(-stone)
        
        heapq.heapify(negative)
        minheap = negative
        
        while len(minheap) > 1:
            heaviest = -heapq.heappop(minheap)
            second = -heapq.heappop(minheap)
            if second < heaviest:
                heaviest -= second
                heapq.heappush(minheap, -heaviest)
        
        if len(minheap) > 0:
            return -heapq.heappop(minheap)
        else:
            return 0
        