class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]

        # make map of positions and speed 
        inputs = [[p,s] for p,s in zip(position, speed)]
        for p,s in sorted(inputs)[::-1]:
            dur = (target-p) / s
            stack.append(dur)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)