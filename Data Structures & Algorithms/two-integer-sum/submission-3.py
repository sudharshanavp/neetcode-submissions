class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            num_dict[nums[i]] = i
        
        for i in nums:
            if target - i in num_dict:
                if nums.index(i) != num_dict[target-i]:
                    return [nums.index(i), num_dict[target-i]]
                