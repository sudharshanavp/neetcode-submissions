class Solution:
    def trap(self, height: List[int]) -> int:
        water, left, right = 0, 0, len(height) - 1
        left_height, right_height = height[left], height[right]
        while left < right:
            if left_height < right_height:
                left += 1
                left_height = max(left_height, height[left])
                water += left_height - height[left] 
            else:
                right -= 1
                right_height = max(right_height, height[right])
                water += right_height - height[right]
        return water
