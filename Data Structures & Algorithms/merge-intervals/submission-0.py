class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # sort the intervals based on intervals[i][0]->start_i
        intervals.sort(key = lambda interval: interval[0])
        for interval in intervals:
            
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]         

        return res