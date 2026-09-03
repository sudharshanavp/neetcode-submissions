class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_counter = defaultdict(int)
        for num in nums:
            if num in duplicate_counter:
                return True
            else:
                duplicate_counter[num] += 1
        return False
        