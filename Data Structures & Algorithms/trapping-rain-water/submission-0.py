class Solution:
    def trap(self, height: List[int]) -> int:
        
        total = 0
        for i in range(len(height)):
            max_left = 0
            max_right = 0
            #find the max left side of i (scan 0 to i)
            for left in range(0, i):
                if max_left < height[left]:
                    max_left=height[left]
            # find max right side of i (scan i+1 to end)    
            for right in range(i+1, len(height)):
                if max_right < height[right]:
                    max_right = height[right]
            water = min(max_left, max_right) - height[i]

            if water > 0:
                total += water

        return total