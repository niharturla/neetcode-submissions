class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(point: List[int]) -> float:
            return math.sqrt(point[0]*point[0] + point[1]*point[1])
        
        heap = [(dist(point), point) for point in points]
        heapq.heapify(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



