class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        maxheight = 0

        while l<r:
            con = min(heights[l], heights[r]) * (r-l)
            maxheight = max(maxheight, con)
             
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxheight
