class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i, j = 0, n - 1
        res = 0
        while i < j:
            width = j - i
            area = min(heights[i], heights[j]) * width
            res = max(res,area)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return(res)