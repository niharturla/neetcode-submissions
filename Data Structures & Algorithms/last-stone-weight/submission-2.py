class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        [2,3,6,2,4]
        6,4 ->2
        [2,3,2,2]
        3,2 -> 1
        [1,2,2]
        2,2->
        [1], return 1
        """

        heapq.heapify_max(stones)

        while len(stones) > 1:
            # pop the first 2
            # x is always >= y
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x >= y:
                heapq.heappush_max(stones, x-y)
        if len(stones) > 0:
            return stones[0]
        return 0