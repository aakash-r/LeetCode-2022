class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxvol = 0
        
        s = 0
        e = len(heights)-1
        curvol = 0
        
        while s<e:
            curvol = min(heights[s],heights[e])*(e-s)
            if heights[s]<heights[e]:
                s+=1
            else:
                e-=1
            maxvol=max(maxvol,curvol)
        return maxvol
                
        