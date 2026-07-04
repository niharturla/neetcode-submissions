class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                height=min(heights[i],heights[j])
                width=j-i
                max_area=max(max_area, height*width)
        return max_area

        