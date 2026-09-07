class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num]+=1
            if frequency[num]>len(nums)/2:
                return num
        