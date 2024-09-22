class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        res=0
        while l<r:
                area=(r-l)*min(height[l],height[r])
                res=max(area,res)
                if height[r]>height[l]:
                    l+=1
                else:
                    r-=1
        return res