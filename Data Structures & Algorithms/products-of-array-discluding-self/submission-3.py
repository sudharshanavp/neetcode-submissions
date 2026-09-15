class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_before = [1] * n
        product_after = [1] * n
        final_result = [1] * n

        for i in range(1, n):
            product_before[i] = nums[i - 1] * product_before[i - 1]
        for i in range(n - 2, -1, -1):
            product_after[i] = nums[i + 1] * product_after[i + 1]
        for i in range(n):
            final_result[i] = product_before[i] * product_after[i]
        
        return final_result

        