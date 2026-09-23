"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda interval: interval.start)
        
        # store end times on minheap
        # if we encouter start time that is >= root of minheap, reduce room by 1
        # every encouter add to min heap

        heap = []
        rooms = 0

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            rooms = max(rooms, len(heap))
                
            
        return rooms
                