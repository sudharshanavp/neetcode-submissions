class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [0] * n
        for num in nums:
            if num > 0 and num <= n:
                seen[num - 1] = 1
            
        for num in range(1, n+1):
            if not seen[num - 1]:
                return num
        
        return n + 1         


        
        