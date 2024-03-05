class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1

        return res
