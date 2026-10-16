class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


    def reverse(self, nums, left, right):
        for i in range((right - left)//2 + 1):
            temp = nums[left + i]
            nums[left + i] = nums[right - i]
            nums[right - i] = temp
