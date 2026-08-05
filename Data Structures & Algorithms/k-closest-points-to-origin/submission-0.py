class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2

        heap = []
        for point in points:
            dist = distance(point)
            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        while heap:
            ans.append(heapq.heappop(heap)[1])
        
        return ans