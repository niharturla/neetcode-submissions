class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        prev_time = 0
        fleets=0
        inputs = [[p,s] for p,s in zip(position, speed)]
        for p,s in sorted(inputs, reverse=True):
            curr_time = (target - p) / s

            if curr_time > prev_time:
                prev_time = curr_time
                fleets += 1
        return fleets
                
                




