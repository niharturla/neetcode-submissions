class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        for i in range(k):
            val = heapq.heappop_max(nums)
        return val