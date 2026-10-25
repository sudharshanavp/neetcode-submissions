class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        res = len(nums) + 1

        while r < len(nums):
            total += nums[r]
            while total >= target:
                total -= nums[l]
                res = min(r - l + 1, res)
                l += 1
            r+=1
        
        return 0 if res == len(nums) + 1 else res

        
