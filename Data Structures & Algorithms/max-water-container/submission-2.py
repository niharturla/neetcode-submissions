class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        left=0
        right=len(heights)-1

        while left < right:
            height=min(heights[left], heights[right])
            width=right-left
            res=max(res,height*width)

            if heights[left] < heights[right]:
                # move left inward
                left += 1
            else:
                right -= 1
        return res



        