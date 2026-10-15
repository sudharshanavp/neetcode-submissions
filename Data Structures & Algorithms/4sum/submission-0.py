class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = length - 1
                while k < l:
                    result = nums[i] + nums[j] + nums[k] + nums[l]
                    if result < target:
                        k += 1
                    elif result > target:
                        l -= 1
                    else:
                        answer.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k < l and nums[k] == nums[k-1]:
                            k+=1
                        while k < l and nums[l] == nums[l+1]:
                            l-=1
        
        return answer