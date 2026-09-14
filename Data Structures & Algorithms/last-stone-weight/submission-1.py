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

        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # pop the first 2
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(y-x))
        if len(stones) > 0:
            return -stones[0]
        return 0