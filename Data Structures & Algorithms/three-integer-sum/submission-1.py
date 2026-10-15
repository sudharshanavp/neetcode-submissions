class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for idx, ele in enumerate(nums):
            if ele > 0:
                break
            if idx> 0 and ele == nums[idx - 1]:
                continue
            
            j, k = idx + 1, len(nums) - 1
            while j < k:
                threeSum = ele + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    answer.append([ele, nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            
        return answer

