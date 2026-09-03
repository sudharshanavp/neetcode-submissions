class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        if len(nums) < 2:
            return False
        for num in nums:
            if num in counter:
                return True
            else:
                counter[num] = 1
        return False
        

        